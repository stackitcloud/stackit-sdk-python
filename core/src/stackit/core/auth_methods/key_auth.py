import atexit
import threading
import time
import uuid
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import Optional

import jwt
import requests
from pydantic import BaseModel, ConfigDict, Field
from requests import Request
from requests.auth import AuthBase


class ServiceAccountKeyCredentials(BaseModel):
    model_config = ConfigDict(strict=True, populate_by_name=True)

    audience: str = Field(alias="aud")
    issuer: str = Field(alias="iss")
    key_id: str = Field(alias="kid")
    private_key: Optional[str] = Field(None, alias="privateKey")
    subject: str = Field(alias="sub")


class ServiceAccountKey(BaseModel):
    model_config = ConfigDict(strict=True)

    active: bool
    created_at: datetime = Field(alias="createdAt")
    credentials: ServiceAccountKeyCredentials
    id: str
    key_algorithm: str = Field(alias="keyAlgorithm")
    key_origin: str = Field(alias="keyOrigin")
    key_type: str = Field(alias="keyType")
    public_key: str = Field(alias="publicKey")
    valid_until: Optional[datetime] = Field(None, alias="validUntil")


class KeyAuth(AuthBase):
    DEFAULT_TOKEN_ENDPOINT = "https://service-account.api.stackit.cloud/token"  # noqa S105 false positive
    TOKEN_EXPIRY_CHECK_INTERVAL = timedelta(seconds=60)
    EXPIRATION_LEEWAY = timedelta(minutes=5)

    timeout: Optional[int] = 30
    initial_token: Optional[str]
    access_token: Optional[str]
    refresh_token: Optional[str]
    token_endpoint: str
    token_expiry_check_interval: int
    lock: threading.Lock
    executor: ThreadPoolExecutor
    refresh_future: Optional[futures.Future]
    service_account_key: ServiceAccountKey

    def __init__(
        self,
        service_account_key: ServiceAccountKey,
        token_endpoint: Optional[str] = None,
    ):
        self.service_account_key = service_account_key
        self.token_endpoint = token_endpoint if token_endpoint else self.DEFAULT_TOKEN_ENDPOINT
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.access_token = None
        self.refresh_future = None
        self.__create_initial_token()
        self.__fetch_token_from_endpoint()
        self.__start_token_refresh_task()

        atexit.register(self.__shutdown)

    def __call__(self, r: Request) -> Request:
        with self.lock:
            if self.__is_token_expired(self.access_token):
                if self.refresh_future is None or self.refresh_future.done():
                    self.refresh_future = self.executor.submit(self.__refresh_token)
            r.headers["Authorization"] = f"Bearer {self.access_token}"
        return r

    def __create_initial_token(self) -> None:
        payload = {
            "iss": self.service_account_key.credentials.issuer,
            "sub": self.service_account_key.credentials.subject,
            "aud": self.service_account_key.credentials.audience,
            "jti": str(uuid.uuid4()),
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=10),
        }
        headers = {"kid": str(self.service_account_key.credentials.key_id)}
        self.initial_token = jwt.encode(
            payload,
            self.service_account_key.credentials.private_key,
            headers=headers,
            algorithm="RS512",
        )

    def __fetch_token_from_endpoint(self) -> None:
        body = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": self.initial_token,
        }
        try:
            response = requests.post(self.token_endpoint, data=body, timeout=self.timeout)
            response.raise_for_status()
            response_json = response.json()
            self.access_token = response_json["access_token"]
            self.refresh_token = response_json["refresh_token"]
        except requests.RequestException as e:
            print(f"Initial token fetch failed: {e}")

    def __start_token_refresh_task(self):
        def token_refresh_task():
            while True:
                time.sleep(self.TOKEN_EXPIRY_CHECK_INTERVAL.total_seconds())
                with self.lock:
                    if self.__is_token_expired(self.access_token) and (
                        self.refresh_future is None or self.refresh_future.done()
                    ):
                        self.refresh_future = self.executor.submit(self.__refresh_token)

        thread = threading.Thread(target=token_refresh_task)
        thread.daemon = True
        thread.start()

    def __refresh_token(self):
        if self.__is_token_expired(self.refresh_token):
            self.__create_initial_token()
            self.__fetch_token_from_endpoint()
            return

        body = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }

        try:
            response = requests.post(self.token_endpoint, data=body, timeout=self.timeout)
            response.raise_for_status()
            response_data = response.json()
            new_token = response_data.get("access_token")
            # with self.lock:
            self.access_token = new_token
            print("Token successfully refreshed!")
        except requests.RequestException as e:
            print(f"Token refresh failed: {e}")

    def __is_token_expired(self, token: str) -> bool:
        try:
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            exp = decoded_token.get("exp")
            if exp:
                return time.time() > (exp + self.EXPIRATION_LEEWAY.total_seconds())
        except jwt.ExpiredSignatureError:
            return True
        except jwt.DecodeError:
            return True
        return False

    def __shutdown(self):
        self.executor.shutdown(wait=False)

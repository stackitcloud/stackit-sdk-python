import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from requests.auth import AuthBase

from stackit.core.auth_methods.key_auth import KeyAuth, ServiceAccountKey
from stackit.core.auth_methods.token_auth import TokenAuth
from stackit.core.configuration import Configuration


class KeyFileIsNotValidError(Exception):
    pass


@dataclass
class Credentials:
    def __init__(
        self,
        STACKIT_SERVICE_ACCOUNT_EMAIL: str = None,
        STACKIT_SERVICE_ACCOUNT_TOKEN: str = None,
        STACKIT_SERVICE_ACCOUNT_KEY_PATH: str = None,
        STACKIT_PRIVATE_KEY_PATH: str = None,
        **kwargs,
    ):
        self.service_account_mail = STACKIT_SERVICE_ACCOUNT_EMAIL
        self.service_account_token = STACKIT_SERVICE_ACCOUNT_TOKEN
        self.service_account_key_path = STACKIT_SERVICE_ACCOUNT_KEY_PATH
        self.private_key_path = STACKIT_PRIVATE_KEY_PATH


class Authorization:
    DEFAULT_CREDENTIALS_FILE_PATH = ".stackit/credentials.json"
    service_account_mail: Optional[str] = None
    service_account_token: Optional[str] = None
    service_account_key: Optional[ServiceAccountKey] = None
    service_account_key_path: Optional[str] = None
    private_key: Optional[str] = None
    private_key_path: Optional[str] = None
    auth_method: Optional[AuthBase] = None

    def __init__(self, configuration: Configuration):
        credentials = self.__read_credentials_file(configuration.credentials_file_path)
        self.service_account_mail = (
            configuration.service_account_mail
            if configuration.service_account_mail is not None
            else credentials.service_account_mail
        )
        self.service_account_token = (
            configuration.service_account_token
            if configuration.service_account_token is not None
            else credentials.service_account_token
        )
        self.service_account_key_path = (
            configuration.service_account_key_path
            if configuration.service_account_key_path is not None
            else credentials.service_account_key_path
        )
        self.private_key_path = (
            configuration.private_key_path
            if configuration.private_key_path is not None
            else credentials.private_key_path
        )
        self.auth_method = configuration.custom_auth
        self.token_endpoint = configuration.token_endpoint
        self.__read_keys()
        self.auth_method = self.__get_authentication()

    def __read_keys(self):
        if self.service_account_key_path and self.service_account_key is None:
            service_account_key_json = self.__read_key_file(self.service_account_key_path)
            self.service_account_key = ServiceAccountKey.model_validate_json(service_account_key_json)
        if self.private_key_path:
            self.private_key = self.__read_key_file(self.private_key_path)
        # Integrate any private key into the service account key
        if (
            self.service_account_key is not None
            and self.service_account_key.credentials.private_key is None
            and self.private_key is not None
        ):
            self.service_account_key.credentials.private_key = self.private_key

    def __get_authentication(self) -> Optional[AuthBase]:
        if self.auth_method:
            return self.auth_method
        elif self.__is_key_auth_possible():
            return KeyAuth(self.service_account_key, self.token_endpoint)
        elif self.service_account_token:
            return TokenAuth(self.service_account_token)
        else:
            return None

    def __is_key_auth_possible(self) -> bool:
        if self.service_account_key is not None and self.service_account_key.credentials.private_key is not None:
            return True
        if self.service_account_key is not None and self.private_key is not None:
            return True
        return False

    def __read_credentials_file(self, file_path: Optional[str]) -> Credentials:
        p = Path(file_path) if file_path else Path.home() / self.DEFAULT_CREDENTIALS_FILE_PATH
        if file_path and (not p.exists() or not p.is_file()):
            raise FileNotFoundError(f"Credentials file at {file_path} does not exist")

        try:
            with open(p, "r") as f:
                content = f.read()
                json_content = json.loads(content)
                return Credentials(**json_content)
        except FileNotFoundError:
            return Credentials()

    def __read_key_file(self, path: str) -> str:
        with open(path, "r") as f:
            key = f.read()
            if len(key) == 0:
                raise KeyFileIsNotValidError(f"Key file is empty: {path}")
            return key

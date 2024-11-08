from requests import Request
from requests.auth import AuthBase


class TokenAuth(AuthBase):
    __access_token: str

    def __init__(self, token: str):
        self.__access_token = token

    def __call__(self, request: Request) -> Request:
        request.headers["Authorization"] = f"Bearer {self.__access_token}"
        return request

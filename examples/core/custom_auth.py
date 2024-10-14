import jwt
from requests import Request
from requests.auth import AuthBase
from stackit.core.configuration import Configuration


"""
You can create your own authorization class to implement your own authorization logic.
You need to derive from the class 'AuthBase' to implement your own class.
"""


class MyAuth(AuthBase):
    __access_token: str

    def __init__(self, key: str):
        self.__access_token = jwt.encode({"some": "payload"}, key, algorithm="HS256")

    def __call__(self, request: Request) -> Request:
        request.headers["Authorization"] = f"Bearer {self.__access_token}"
        return request


# Initialize custom auth method
auth_method = MyAuth(key="my_super_secret_key")
# Set it in the configuration
config = Configuration(custom_auth=auth_method)

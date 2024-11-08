from pathlib import Path, PurePath

import pytest
import json
from unittest.mock import patch, mock_open, Mock

from requests.auth import HTTPBasicAuth

from stackit.core.auth_methods.key_auth import KeyAuth
from stackit.core.auth_methods.token_auth import TokenAuth
from stackit.core.authorization import Authorization
from stackit.core.configuration import Configuration


DEFAULT_EMAIL = "email"
DEFAULT_PRIVATE_KEY_PATH = "/path/to/private.key"
DEFAULT_SERVICE_ACCOUNT_TOKEN = "token"
DEFAULT_SERVICE_ACCOUNT_KEY_PATH = "/path/to/account.key"


@pytest.fixture
def empty_credentials_file_json():
    return """{
}"""


@pytest.fixture
def credentials_file_json():
    return """{
    "STACKIT_SERVICE_ACCOUNT_EMAIL": "email",
    "STACKIT_PRIVATE_KEY_PATH": "/path/to/private.key",
    "STACKIT_SERVICE_ACCOUNT_TOKEN": "token",
    "STACKIT_SERVICE_ACCOUNT_KEY_PATH": "/path/to/account.key"
}"""


@pytest.fixture
def service_account_key_file_json():
    """
    This test key is for testing purposes only.
    It does not hold any real private key that can be exploited.
    :return: A JSON representation of the service account key
    """
    return """{
    "id": "37d5807c-f878-478a-97f6-231bd9d8bb65",
    "publicKey": "-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr/9VaXHGxFjX1qrb3m4v\\naKkWRDNuqDgWmiE9PArcK34cr98eE3e6q0x6bJ1zwDQBhG1UHITbJ1QOSAnIWCDc\\nzh/lqZ9tMg/EruQQzQloVweRAiz1LpKiExc/7UyX2hI1Tw3VvCczqB5jZifBLQre\\nTEktpImA26fkOVP3/3HaXPuQiUcPx9BulgVkmfcTY8RXSlQja//R1iqbIULCaXXs\\nIzNJrGqg0Mf37Wout+lfjjrOul/8wuA1urD5Hv511yQxlnAooLktrw+hDtb6BLhA\\nb+XTklFKGKmSuPig4nQKUsZrYSmMWb2rRi3EOdOzIwy3/mqVZgtYtSsfHix10GSP\\nMQIDAQAB\\n-----END PUBLIC KEY-----",
    "createdAt": "2024-01-01T00:00:00.000+00:00",
    "validUntil": "2099-12-31T23:59:59.999+00:00",
    "keyType": "USER_MANAGED",
    "keyOrigin": "GENERATED",
    "keyAlgorithm": "RSA_2048",
    "active": true,
    "credentials": {
        "kid": "35b250fb-3186-47ca-8dc2-1b4632272785",
        "iss": "pytest-test-3wv29m1@sa.stackit.cloud",
        "sub": "cafba1a4-7c00-4206-bb2d-b566968bb026",
        "aud": "https://stackit-service-account-prod.apps.01.cf.eu01.stackit.cloud"
    }
}"""  # noqa: E501 long publicKey


@pytest.fixture
def private_key_file():
    """
    This private key was generated from scratch and cannot be used as part of a
    service account key
    :return: A base64 encoded text representation of the private key
    """
    return """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv/1VpccbEWNfW
qtvebi9oqRZEM26oOBaaIT08Ctwrfhyv3x4Td7qrTHpsnXPANAGEbVQchNsnVA5I
CchYINzOH+Wpn20yD8Su5BDNCWhXB5ECLPUukqITFz/tTJfaEjVPDdW8JzOoHmNm
J8EtCt5MSS2kiYDbp+Q5U/f/cdpc+5CJRw/H0G6WBWSZ9xNjxFdKVCNr/9HWKpsh
QsJpdewjM0msaqDQx/ftai636V+OOs66X/zC4DW6sPke/nXXJDGWcCiguS2vD6EO
1voEuEBv5dOSUUoYqZK4+KDidApSxmthKYxZvatGLcQ507MjDLf+apVmC1i1Kx8e
LHXQZI8xAgMBAAECggEAGiZUgP3MPDk9HKK3V3XEqobRDaIcs3bd+NmueQDeFMJA
rer3U4orHK+Y0xGT9L9laFE8OZ6N12qYUqDNeTasyB2aKJlNBq6sGRY+3tAihifU
JmAar+hOl4qRT4ddWqPw8sWJ99JVTQny1+dZPwGJ5QjMdNGPaVOpR9FPnE9E1CK3
j/Vxl2ERwz36H6zcgHx8NaHTwPvj7lJBjb3iYvsRESLt4FCgP+/T9M0ZSsvT0A09
bXCvBWBtoZP8zr8w2lNTNG2tQeevc0Z06dbNPvjT2HOHE1s7BVXvk+jtbfOy47dC
go42slozS1/SBV1Yh/WyMJvLuh/QOzjoTj/t5JAWKQKBgQDY9YwChD5BVWr/QcIj
oRHYryVUuXuv0RoVARKF4NfZFI1r/j0kZgGLm6+r4/MEAzZ44tKIHn4v+tLuEfhe
E49zhdVBb+aiGDiOGP7XdhGGvWXb4/uTTQBBlnlWyDSu9HJzLOx1vjyJVPtyDE4X
42v8YDOyQI90WCSWDwDB+x7TNQKBgQDPqtbrAzjCpqD1cyeQOexanKd0q/qwvkYD
s1X4+LufjzTo/epg9/NyoB/N7a8fJQlD6EvjnHHSlrhfWA5K7/DgFzu6XSmHqO4g
IxV7EaBvBqhqBQ7QFbwklxf/9FVx3KXo7zHlLidE5JZiSe6PL74fDWiopywKJC7C
Lv0c1gWvjQKBgQDUNI9mIrzVoFuQIVxnBvLyspTb4rQUynwtUSgx5DKa9BxDJZ/e
Cxu11mgjw0h9gzrzUD/FvbWE7lsDWnZIZe9oed2VLIMzxmcCrXYNfkE0Pen0AnCd
qbH3dNtnw1isSxHqj2UU4SZK2OE7ssdrXBjR97J4xebKUDAwyanfEeUbhQKBgQCW
yGOuVjODWftq3IbweK49iJsp4qluZWluzGrzEJ8ilpeDSMJCUCaKpusQ2bCau4iD
rwpTJMeccWVDjSsrjBZoj1YF1hkOcEEeQnsZVc4Yb0wfVrbPrchjBPYfGWhk+SHa
BLtEvYMzyYnLqgS2IKM55sGEG4Wlg2oUAowzwM52DQKBgHtJ78HmvKTAYxjmvHnI
4oUjXnJNjdbgO4SDVvetWxS1pDUfOP4VW6+WUexpTNG7f8FICWuZ1csg0m7FprsW
A0JfCMXgAMnUeYaEO600z2aDlT09koxI8OgOA/zwkwbgfg86xC6ejV+b+rCkUyr+
VT4CLlEvtB5DvFNuoRn2nvcQ
-----END PRIVATE KEY-----
"""


@pytest.fixture
def access_token_post_request():
    with patch("requests.post") as mock_post:
        mock_response_success = Mock()
        mock_response_success.status_code = 200
        mock_response_success.json.return_value = {
            "access_token": "eyJhbGciOiJSUzUxMiIsImtpZCI6IjM1YjI1MGZiLTMxODYtNDdjYS04ZGMyLTFiNDYzMjI3Mjc4NSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJweXRlc3QtdGVzdC0zd3YyOW0xQHNhLnN0YWNraXQuY2xvdWQiLCJzdWIiOiJjYWZiYTFhNC03YzAwLTQyMDYtYmIyZC1iNTY2OTY4YmIwMjYiLCJhdWQiOiJodHRwczovL3N0YWNraXQtc2VydmljZS1hY2NvdW50LXByb2QuYXBwcy4wMS5jZi5ldTAxLnN0YWNraXQuY2xvdWQiLCJqdGkiOiJhZWMzZDQ5NC1lYzgyLTQzNmQtOGE0OS0zZDMxNGI0YzhkMjkiLCJpYXQiOjE3MjY1NzgwNjIsImV4cCI6MTcyNjU3ODY2Mn0.SSnbSkhWXmURYhktv3g5g5fnsn4UgqAhLKdbL75bg67d-3b2R3ZPfX__lPP1VlrCuzEXtNkcL1nXsd-QR4qTHJp17dtr9B7vRgtZVKtwky2bd3gNYT_4lfYV3WMJWxfsqT_khbFEfPtr70fmwiaWA__2YOwd78rl78bFetPVhHEmMzlEoCWS4cK4Im2xzKTD5J1f0HnTs1rR-EtCHeKXRrst8OF8IVz6mrvVVq0LBJh2HI1rLSvLpJBR-B3C9dlDMJk7KC5fztOd_zunYqVOs_JmsimVbJyZYXqwCVmFnagvZWMjftaajFIJnXYfLhiy2blwXr7aHiDWwg8EspvTMw",  # noqa: E501 long token
            "refresh_token": "eyJhbGciOiJSUzUxMiIsImtpZCI6IjM1YjI1MGZiLTMxODYtNDdjYS04ZGMyLTFiNDYzMjI3Mjc4NSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJweXRlc3QtdGVzdC0zd3YyOW0xQHNhLnN0YWNraXQuY2xvdWQiLCJzdWIiOiJjYWZiYTFhNC03YzAwLTQyMDYtYmIyZC1iNTY2OTY4YmIwMjYiLCJhdWQiOiJodHRwczovL3N0YWNraXQtc2VydmljZS1hY2NvdW50LXByb2QuYXBwcy4wMS5jZi5ldTAxLnN0YWNraXQuY2xvdWQiLCJqdGkiOiJhZWMzZDQ5NC1lYzgyLTQzNmQtOGE0OS0zZDMxNGI0YzhkMjkiLCJpYXQiOjE3MjY1NzgwNjIsImV4cCI6MTcyNjU3ODY2Mn0.SSnbSkhWXmURYhktv3g5g5fnsn4UgqAhLKdbL75bg67d-3b2R3ZPfX__lPP1VlrCuzEXtNkcL1nXsd-QR4qTHJp17dtr9B7vRgtZVKtwky2bd3gNYT_4lfYV3WMJWxfsqT_khbFEfPtr70fmwiaWA__2YOwd78rl78bFetPVhHEmMzlEoCWS4cK4Im2xzKTD5J1f0HnTs1rR-EtCHeKXRrst8OF8IVz6mrvVVq0LBJh2HI1rLSvLpJBR-B3C9dlDMJk7KC5fztOd_zunYqVOs_JmsimVbJyZYXqwCVmFnagvZWMjftaajFIJnXYfLhiy2blwXr7aHiDWwg8EspvTMw",  # noqa: E501 long token
            "scope": "",
            "token_type": "Bearer",
            "expires_in": 3600,
        }

        mock_response_error = Mock()
        mock_response_error.status_code = 400
        mock_response_error.json.return_value = {
            "status": "error",
            "message": "Bad Request",
        }

        # Customize mock behavior based on the URL or request data
        def post_side_effect(url, data, *args, **kwargs):
            if (
                url == "https://service-account.api.stackit.cloud/token"
                and data["grant_type"] == "urn:ietf:params:oauth:grant-type:jwt-bearer"
                and data["assertion"].startswith("ey")
            ):
                return mock_response_success
            else:
                return mock_response_error

        # Assign the side effect to the mock
        mock_post.side_effect = post_side_effect

        # Yield the mock to be used in tests
        yield mock_post


real_open = open  # We need this to allow a non-mocked open() to work correctly


def mock_open_function(
    filepath: PurePath,
    credentials_file_json,
    service_account_key_file_json,
    private_key_file,
    *args,
    **kwargs,
):
    path = str(filepath)
    if path.endswith(Authorization.DEFAULT_CREDENTIALS_FILE_PATH):
        f_open = mock_open(read_data=credentials_file_json)
    elif path == DEFAULT_SERVICE_ACCOUNT_KEY_PATH:
        f_open = mock_open(read_data=service_account_key_file_json)
    elif path == DEFAULT_PRIVATE_KEY_PATH:
        f_open = mock_open(read_data=private_key_file)
    else:
        f_open = real_open
    return f_open(filepath, *args, **kwargs)


class TestAuth:
    def test_token_auth_is_selected_when_token_is_given(self, empty_credentials_file_json):
        with patch("builtins.open", mock_open(read_data=empty_credentials_file_json)):
            config = Configuration(service_account_token="token")
            auth = Authorization(config)
            assert type(auth.auth_method) is TokenAuth

    def test_no_auth_is_selected_when_no_configuration_is_given(self, empty_credentials_file_json):
        with patch("builtins.open", mock_open(read_data=empty_credentials_file_json)):
            config = Configuration()
            auth = Authorization(config)
            assert auth.auth_method is None

    def test_given_nonexistent_credentials_file_raises_filenotfound_exception(self):
        config = Configuration(credentials_file_path="/non/existent/path/to/file")
        with pytest.raises(FileNotFoundError):
            Authorization(config)

    def test_nonexistent_default_credentials_file_raises_no_exception(self, monkeypatch):
        def mockreturn():
            return Path("/this/path/does/not/exist/")

        monkeypatch.setattr(Path, "home", mockreturn)
        config = Configuration()
        auth = Authorization(config)
        assert auth.auth_method is None

    def test_valid_credentials_file_is_parsed(
        self, credentials_file_json, service_account_key_file_json, private_key_file
    ):
        with patch(
            "builtins.open",
            lambda filepath, *args, **kwargs: mock_open_function(
                filepath,
                credentials_file_json,
                service_account_key_file_json,
                private_key_file,
            ),
        ):
            config = Configuration(custom_auth=HTTPBasicAuth("test", "test"))
            auth = Authorization(configuration=config)
            assert auth.service_account_mail == DEFAULT_EMAIL
            assert auth.service_account_token == DEFAULT_SERVICE_ACCOUNT_TOKEN
            assert auth.service_account_key_path == DEFAULT_SERVICE_ACCOUNT_KEY_PATH
            assert auth.private_key_path == DEFAULT_PRIVATE_KEY_PATH

    def test_valid_token_is_generated_from_service_account_key(
        self,
        credentials_file_json,
        service_account_key_file_json,
        private_key_file,
        access_token_post_request,
    ):
        with patch(
            "builtins.open",
            lambda filepath, *args, **kwargs: mock_open_function(
                filepath,
                credentials_file_json,
                service_account_key_file_json,
                private_key_file,
            ),
        ):
            config = Configuration()
            auth = Authorization(config)
            assert type(auth.auth_method) is KeyAuth

    def test_invalid_credentials_file_is_rejected(self, credentials_file_json):
        malformed_json = credentials_file_json.replace(":", "=")
        with patch("builtins.open", mock_open(read_data=malformed_json)):
            config = Configuration()
            with pytest.raises(json.JSONDecodeError):
                Authorization(config)

    def test_private_keyfile_not_found_raises_exception(self):
        config = Configuration(private_key_path="/non/existent/path/to/file")
        with pytest.raises(FileNotFoundError):
            Authorization(config)

    def test_service_account_keyfile_not_found_raises_exception(self):
        config = Configuration(service_account_key_path="/non/existent/path/to/file")
        with pytest.raises(FileNotFoundError):
            Authorization(config)

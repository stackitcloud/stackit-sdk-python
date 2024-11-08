import pytest

from stackit.core.configuration import Configuration


SERVICE_ACCOUNT_EMAIL = "test@example.org"
SERVICE_ACCOUNT_TOKEN = "token"
SERVICE_ACCOUNT_KEY_PATH = "/path/to/account/key"
PRIVATE_KEY_PATH = "/path/to/private/key"
TOKEN_BASEURL = "http://localhost:8000"
CREDENTIALS_PATH = "/path/to/credentials"
REGION = "test-region"


@pytest.fixture()
def config_envs(monkeypatch):
    monkeypatch.setenv("STACKIT_SERVICE_ACCOUNT_EMAIL", SERVICE_ACCOUNT_EMAIL)
    monkeypatch.setenv("STACKIT_SERVICE_ACCOUNT_TOKEN", SERVICE_ACCOUNT_TOKEN)
    monkeypatch.setenv("STACKIT_SERVICE_ACCOUNT_KEY_PATH", SERVICE_ACCOUNT_KEY_PATH)
    monkeypatch.setenv("STACKIT_PRIVATE_KEY_PATH", PRIVATE_KEY_PATH)
    monkeypatch.setenv("STACKIT_TOKEN_BASEURL", TOKEN_BASEURL)
    monkeypatch.setenv("STACKIT_CREDENTIALS_PATH", CREDENTIALS_PATH)
    monkeypatch.setenv("STACKIT_REGION", REGION)


class TestConfig:
    def test_check_if_environment_is_set(self, config_envs):
        config = Configuration()
        assert config.service_account_mail == SERVICE_ACCOUNT_EMAIL
        assert config.service_account_token == SERVICE_ACCOUNT_TOKEN
        assert config.service_account_key_path == SERVICE_ACCOUNT_KEY_PATH
        assert config.private_key_path == PRIVATE_KEY_PATH
        assert config.region == REGION

    def test_check_valid_server_index(self):
        config = Configuration()
        assert config.server_index == 0

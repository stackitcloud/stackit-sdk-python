import os


class EnvironmentVariables:
    SERVICE_ACCOUNT_EMAIL_ENV = "STACKIT_SERVICE_ACCOUNT_EMAIL"
    SERVICE_ACCOUNT_TOKEN_ENV = "STACKIT_SERVICE_ACCOUNT_TOKEN"  # noqa: S105 false positive
    SERVICE_ACCOUNT_KEY_PATH_ENV = "STACKIT_SERVICE_ACCOUNT_KEY_PATH"
    PRIVATE_KEY_PATH_ENV = "STACKIT_PRIVATE_KEY_PATH"
    TOKEN_BASEURL_ENV = "STACKIT_TOKEN_BASEURL"  # noqa: S105 false positive
    CREDENTIALS_PATH_ENV = "STACKIT_CREDENTIALS_PATH"
    REGION_ENV = "STACKIT_REGION"

    def __init__(self):
        self.account_email = os.environ.get(self.SERVICE_ACCOUNT_EMAIL_ENV)
        self.service_account_token = os.environ.get(self.SERVICE_ACCOUNT_TOKEN_ENV)
        self.account_key_path = os.environ.get(self.SERVICE_ACCOUNT_KEY_PATH_ENV)
        self.private_key_path = os.environ.get(self.PRIVATE_KEY_PATH_ENV)
        self.token_baseurl = os.environ.get(self.TOKEN_BASEURL_ENV)
        self.credentials_path = os.environ.get(self.CREDENTIALS_PATH_ENV)
        self.region = os.environ.get(self.REGION_ENV)


class Configuration:
    def __init__(
        self,
        region=None,
        service_account_mail=None,
        service_account_token=None,
        service_account_key=None,
        service_account_key_path=None,
        private_key=None,
        private_key_path=None,
        credentials_file_path=None,
        custom_endpoint=None,
        custom_http_session=None,
        custom_auth=None,
        server_index=None,
    ) -> None:
        environment_variables = EnvironmentVariables()
        self.region = region if region else environment_variables.region
        self.token_endpoint = environment_variables.token_baseurl
        self.service_account_token = (
            environment_variables.service_account_token if service_account_token is None else service_account_token
        )
        self.service_account_mail = (
            environment_variables.account_email if service_account_mail is None else service_account_mail
        )
        self.service_account_key = service_account_key
        self.service_account_key_path = (
            environment_variables.account_key_path if service_account_key_path is None else service_account_key_path
        )
        self.private_key = private_key
        self.private_key_path = environment_variables.private_key_path if private_key_path is None else private_key_path
        self.credentials_file_path = (
            environment_variables.credentials_path if credentials_file_path is None else credentials_file_path
        )
        self.custom_endpoint = custom_endpoint
        self.custom_http_session = custom_http_session
        self.custom_auth = custom_auth
        self.server_index = server_index if server_index else 0

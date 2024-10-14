from stackit.core.configuration import Configuration

"""
You can configure you own access token (which is also called service account token).
Do note that if you configure a token, a service acccount key will still be used, if possible.
"""
config = Configuration(service_account_token="my_access_token")  # noqa: S106

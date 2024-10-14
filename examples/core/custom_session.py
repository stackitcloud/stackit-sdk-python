import requests
from requests.adapters import HTTPAdapter
from stackit.core.configuration import Configuration
from urllib3 import Retry

"""
This example shows how to configure the retry count and options.
If you need fine-grained control for the retry logic, you can use urllib3's Retry.
If you just want to increase the retry count, you can use an integer instead.
"""
retries = Retry(
    total=30,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={"POST"},
)
# Create a new custom session
custom_session = requests.Session()
# Set the retry configuration for the session
custom_session.mount("http://", HTTPAdapter(max_retries=retries))
# You can also set the retry count directly. You don't need to use Retry in this case.
custom_session.mount("https://", HTTPAdapter(max_retries=5))
# Set the session in the configuration which is used for all requests from now on
config = Configuration(custom_http_session=custom_session)

"""
This example uses a custom Requests session to configure the timeout of requests.
"""


class CustomSession(requests.Session):
    def __init__(self, timeout: int):
        self.timeout = timeout
        super().__init__()

    def request(self, method, url, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        return super().request(method, url, **kwargs)


custom_session2 = CustomSession(timeout=5)
config2 = Configuration(custom_http_session=custom_session2)

"""
You can even use both examples together to have more fine-grained control over the requests.
"""
custom_session3 = CustomSession(timeout=5)
custom_session3.mount("http://", HTTPAdapter(max_retries=retries))
custom_session3.mount("https://", HTTPAdapter(max_retries=retries))
config3 = Configuration(custom_http_session=custom_session3)

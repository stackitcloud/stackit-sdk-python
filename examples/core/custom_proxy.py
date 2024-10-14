from typing import Dict
import requests
from stackit.core.configuration import Configuration

# Set the proxy servers here. You can set 'http', 'https' and 'ftp'.
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.11:1080",
}


class CustomSession(requests.Session):
    def __init__(self, proxies: Dict[str, str]):
        self.proxies = proxies
        super().__init__()

    def request(self, method, url, **kwargs):
        if "proxies" not in kwargs:
            kwargs["proxies"] = self.proxies
        return super().request(method, url, **kwargs)


custom_session = CustomSession(proxies=proxies)
config = Configuration(custom_http_session=custom_session)

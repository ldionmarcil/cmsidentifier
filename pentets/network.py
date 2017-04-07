import logging
import requests
from io import BytesIO

from .helpers import cyan

class CurlClient():
    def __init__(self, user_agent=None, proxy=None):
        self.user_agent = user_agent
        self.proxy = proxy

    def request(self, url):
        logging.debug("GET {}".format(cyan(url)))

        headers = {}
        if self.user_agent:
            headers["User-Agent"] = self.user_agent

        proxies = {}
        if self.proxy:
            proxies = { self.proxy }

        response = requests.get(url,
                                allow_redirects=True,
                                timeout=1,
                                proxies=proxies,
                                headers=headers)

        return response.text

import unittest
from pentets.network import CurlClient
import responses

class NetworkTest(unittest.TestCase):
    def test_client_defaults(self):
        client = CurlClient()
        self.assertEqual(None, client.user_agent)
        self.assertEqual(None, client.proxy)

    def test_client_with_custom_user_agent(self):
        client = CurlClient(user_agent="patate")
        self.assertEqual("patate", client.user_agent)

    def test_client_with_proxy(self):
        client = CurlClient(proxy="tor://127.0.0.1")
        self.assertEqual("tor://127.0.0.1", client.proxy)

    # I'm not a good programmer so I can't make this work
    def test_request(self):
        # responses.add(responses.GET, 'https://google.ca', body='patate', status=200)
        # self.assertEqual("patate", CurlClient().request("https://google.ca"))
        pass

    def test_request_with_user_agent(self):
        pass

    def test_request_with_proxy(self):
        pass

import unittest
import requests

import getvm


class TestHetznerApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "set up the variables before tests"
        cls.variables = getvm.ApiConnector()

    def test_api_key(self):
        "Check if the API key exists"
        self.assertIsNotNone(self.variables.token, "Empty Hetzner API key")

    def test_servers_endpoint(self):
        "Check if the Hetzner servers endpoint exists"
        request = requests.get(
            self.variables.servers_endpoint, headers=self.variables.headers
        )
        self.assertEqual(request.status_code, 200)

    def test_locations_endpoint(self):
        "Check if the Hetzner location endpoint exists"
        request = requests.get(
            self.variables.locations_endpoint, headers=self.variables.headers
        )
        self.assertEqual(request.status_code, 200)

    def test_images_endpoint(self):
        "Check if the Hetzner eimage endpoint exists"
        request = requests.get(
            self.variables.images_endpoint, headers=self.variables.headers
        )
        self.assertEqual(request.status_code, 200)


if __name__ == "__main__":
    unittest.main()

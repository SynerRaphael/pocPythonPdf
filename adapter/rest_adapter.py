import requests

class apiAdapter:

    def __init__(self, api_url):
        self.api_url = api_url

    def get_request(self):
        return requests.get(self.api_url)
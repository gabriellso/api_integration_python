import requests
from configs.settings import API_URL, API_TOKEN

class APIClient:
    def __init__(self):
        self.base_url = API_URL
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return self._handle_response(response)

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"Erro HTTP: {err}")
        except ValueError:
            print("Resposta não é JSON!")
        return None

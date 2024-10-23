import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
from requests.auth import HTTPBasicAuth

class APIImplementation:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get_data(self, endpoint):
        full_url = f"{self.base_url}{endpoint}"
        print(f"Making request to: {full_url}")
        try:
            response = requests.get(full_url, auth=HTTPBasicAuth(self.username, self.password))
            response.raise_for_status()
            return response.json()
        except ConnectionError:
            print(f"Connection error: unable to connect to {full_url}. Check your network or API address.")
        except Timeout:
            print(f"Timeout error: the server took too long to respond to {full_url}. Try again later.")
        except RequestException as e:
            print(f"Request error: {e}. Check the request parameters or the API service.")
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}. Response content: {response.content}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return []

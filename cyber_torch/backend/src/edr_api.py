import os
import requests
from dotenv import load_dotenv

load_dotenv()

class EDRClient:
    def __init__(self):
        self.edr_url = os.getenv('EDR_URL')
        self.api_key = os.getenv('EDR_API_KEY')

    def push_to_edr(self, data):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        try:
            response = requests.post(self.edr_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error pushing to EDR: {e}")
            return None

    def pull_from_edr(self):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.get(self.edr_url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error pulling from EDR: {e}")
            return None

# Example usage
# edr_client = EDRClient()
# edr_client.push_to_edr(data)
# edr_client.pull_from_edr() 
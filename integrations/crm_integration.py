import requests

class CRMIntegration:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def create_lead(self, lead_info):
        if not lead_info:
            raise ValueError("Lead information is required")

        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(f"{self.base_url}/leads", json=lead_info, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error creating lead: {response.text}")

        return response.json()

    def update_lead(self, lead_id, lead_info):
        if not lead_id or not lead_info:
            raise ValueError("Lead ID and information are required")

        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.put(f"{self.base_url}/leads/{lead_id}", json=lead_info, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error updating lead: {response.text}")

        return response.json()

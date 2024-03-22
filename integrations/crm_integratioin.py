import requests


class CRMIntegration:

  def __init__(self, api_url, api_key):
    self.api_url = api_url
    self.api_key = api_key

  def retrieve_customer_data(self, customer_id):
    if not customer_id:
      raise ValueError("Customer ID is required to retrieve data.")

    try:
      response = requests.get(
          f"{self.api_url}/customers/{customer_id}",
          headers={'Authorization': f'Bearer {self.api_key}'})
      response.raise_for_status()
      return response.json()
    except Exception as e:
      print(f"Error retrieving data for customer {customer_id}: {e}")
      return None

  def update_customer_record(self, customer_id, data):
    if not customer_id or not data:
      raise ValueError("Customer ID and data are required to update a record.")

    try:
      response = requests.put(
          f"{self.api_url}/customers/{customer_id}",
          headers={'Authorization': f'Bearer {self.api_key}'},
          json=data)
      response.raise_for_status()
      return response.json()
    except Exception as e:
      print(f"Error updating record for customer {customer_id}: {e}")
      return None

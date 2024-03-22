import requests


class SchedulingIntegration:

  def __init__(self, api_url, api_key):
    self.api_url = api_url
    self.api_key = api_key

  def schedule_appointment(self, customer_id, datetime, details):
    if not customer_id or not datetime:
      raise ValueError(
          "Customer ID and datetime are required to schedule an appointment.")

    data = {
        'customer_id': customer_id,
        'datetime': datetime,
        'details': details
    }

    try:
      response = requests.post(
          f"{self.api_url}/appointments",
          headers={'Authorization': f'Bearer {self.api_key}'},
          json=data)
      response.raise_for_status()
      return response.json()
    except Exception as e:
      print(f"Error scheduling appointment for customer {customer_id}: {e}")
      return None

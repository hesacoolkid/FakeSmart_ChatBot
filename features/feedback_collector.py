from database.firestore_client import FirestoreClient
from datetime import datetime  # Import the datetime class


class FeedbackCollector:

  def __init__(self, db: FirestoreClient):
    self.db = db

  def collect_feedback(self, customer_id, feedback):
    if not customer_id or not feedback:
      raise ValueError("Customer ID and feedback are required.")

    try:
      feedback_data = {
          'customer_id': customer_id,
          'feedback': feedback,
          'timestamp': datetime.now()  # Corrected to datetime class
      }
      self.db.update_user_history(customer_id, {'feedback': feedback_data})
      print(f"Feedback collected for customer {customer_id}.")
    except Exception as e:
      print(f"Error collecting feedback: {e}")

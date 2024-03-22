import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)


class FirestoreClient:

  def __init__(self):
    self.db = firestore.client()

  def get_user_data(self, customer_id):
    """
        Retrieves user data from Firestore based on the customer ID.

        Args:
            customer_id (str): The unique customer ID.

        Returns:
            dict: The user data if found, None otherwise.
        """
    doc_ref = self.db.collection('users').document(customer_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

  def create_user(self, customer_id, user_data):
    """
        Creates a new user record in Firestore.

        Args:
            customer_id (str): The unique customer ID.
            user_data (dict): The data to store for the user.
        """
    doc_ref = self.db.collection('users').document(customer_id)
    doc_ref.set(user_data)
    print(f"User {customer_id} created in Firestore.")

  def update_user_history(self, customer_id, interaction_data):
    """
        Updates the user's interaction history in Firestore.

        Args:
            customer_id (str): The unique customer ID.
            interaction_data (dict): The interaction data to update.
        """
    doc_ref = self.db.collection('users').document(customer_id)
    doc_ref.update({'history': firestore.ArrayUnion([interaction_data])})
    print(f"User {customer_id} interaction history updated in Firestore.")

  def get_user_history(self, customer_id):
    """
        Retrieves the interaction history for a user from Firestore.

        Args:
            customer_id (str): The unique customer ID.

        Returns:
            list: The user's interaction history if found, None otherwise.
        """
    doc_ref = self.db.collection('users').document(customer_id)
    doc = doc_ref.get()
    return doc.to_dict().get('history') if doc.exists else None

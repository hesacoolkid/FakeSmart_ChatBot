import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreClient:
    def __init__(self):
        # Initialize Firebase Admin SDK with your project's credentials
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_user_data(self, customer_id):
        """
        Fetch user data from Firestore using the customer ID.

        Args:
            customer_id (str): The customer's unique identifier.

        Returns:
            dict: User data if found, None otherwise.
        """
        doc_ref = self.db.collection('users').document(customer_id)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else None

    def update_user_data(self, customer_id, data):
        """
        Update user data in Firestore.

        Args:
            customer_id (str): The customer's unique identifier.
            data (dict): Data to update.
        """
        doc_ref = self.db.collection('users').document(customer_id)
        doc_ref.set(data, merge=True)

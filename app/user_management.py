import logging
from utilities.hashing_utils import generate_customer_id
from database.firestore_client import FirestoreClient

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the Firestore client
db = FirestoreClient()


def identify_user(user_info):
  """
    Identifies a user based on provided information and returns a unique customer ID.

    Args:
        user_info (str): Information about the user (e.g., email or phone number).

    Returns:
        str: A unique customer ID.
    """
  if not user_info:
    logging.error("No user information provided for identification.")
    return None

  # Generate a unique ID for the user based on their info
  customer_id = generate_customer_id(user_info)

  try:
    # Check if the user already exists in the database and retrieve their data
    user_data = db.get_user_data(customer_id)

    if not user_data:
      # If the user doesn't exist, create a new entry in the database
      db.create_user(customer_id, {"info": user_info})
      logging.info(f"New user created in the database with ID: {customer_id}")
  except Exception as e:
    logging.error(f"Error identifying user: {e}")
    return None

  return customer_id


def get_user_history(customer_id):
  """
    Retrieves the chat history or interaction history of the user.

    Args:
        customer_id (str): The unique customer ID.

    Returns:
        dict: The user's interaction history.
    """
  if not customer_id:
    logging.error("No customer ID provided for retrieving user history.")
    return None

  try:
    return db.get_user_history(customer_id)
  except Exception as e:
    logging.error(f"Error retrieving user history for {customer_id}: {e}")
    return None


def update_user_interaction(customer_id, interaction_data):
  """
    Updates the interaction history for the user.

    Args:
        customer_id (str): The unique customer ID.
        interaction_data (dict): Data to be added to the user's interaction history.
    """
  if not customer_id or not interaction_data:
    logging.error(
        "Customer ID or interaction data missing for updating user interaction."
    )
    return

  try:
    db.update_user_history(customer_id, interaction_data)
    logging.info(f"User interaction updated for {customer_id}.")
  except Exception as e:
    logging.error(f"Error updating interaction for {customer_id}: {e}")

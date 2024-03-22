import hashlib


def generate_customer_id(user_info):
  """
    Generates a unique customer ID by hashing the provided user information.

    Args:
        user_info (str): The user information (e.g., email or phone number) to hash.

    Returns:
        str: A hashed string representing the customer ID.
    """
  if not user_info:
    raise ValueError(
        "User information is required for generating a customer ID.")

  # Normalize and encode the user information to ensure consistent hashing
  normalized_info = user_info.strip().lower().encode('utf-8')

  # Create a SHA-256 hash of the normalized information
  hash_object = hashlib.sha256(normalized_info)
  customer_id = hash_object.hexdigest()

  return customer_id

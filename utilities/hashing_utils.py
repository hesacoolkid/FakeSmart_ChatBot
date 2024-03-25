import hashlib

def generate_customer_id(user_info):
    """
    Generate a unique customer ID based on user information.

    Args:
        user_info (str): Information about the user, such as email or phone number.

    Returns:
        str: A unique customer ID.
    """
    if not user_info:
        raise ValueError("User information is required to generate a customer ID.")
    
    # Use SHA-256 hashing to generate a unique identifier
    return hashlib.sha256(user_info.encode('utf-8')).hexdigest()

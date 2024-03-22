from cryptography.fernet import Fernet

# It's important to securely store and manage this key
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)


def encrypt_data(data):
  if not data:
    raise ValueError("Data is required for encryption.")
  try:
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data
  except Exception as e:
    print(f"Error encrypting data: {e}")
    return None


def decrypt_data(encrypted_data):
  if not encrypted_data:
    raise ValueError("Encrypted data is required for decryption.")
  try:
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()
  except Exception as e:
    print(f"Error decrypting data: {e}")
    return None

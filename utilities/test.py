# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key.decode())


import os

# Print the path to the service account key file
print("GOOGLE_APPLICATION_CREDENTIALS:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

import os
from cryptography.fernet import Fernet

key = os.getenv('FERNET_KEY')
if key is None:
    raise ValueError("FERNET_KEY environment variable is not set.")

# Decode the key from base64
key_bytes = key.encode('utf-8')
fernet_key = Fernet(key_bytes)

class EncryptionUtils:
    def __init__(self, cipher_suite):
        self.cipher_suite = cipher_suite

    def encrypt(self, text):
        if not text:
            raise ValueError("No text provided for encryption.")
        text_bytes = text.encode('utf-8')
        encrypted_text = self.cipher_suite.encrypt(text_bytes)
        return encrypted_text.decode('utf-8')

    def decrypt(self, encrypted_text):
        if not encrypted_text:
            raise ValueError("No encrypted text provided for decryption.")
        encrypted_text_bytes = encrypted_text.encode('utf-8')
        decrypted_text = self.cipher_suite.decrypt(encrypted_text_bytes)
        return decrypted_text.decode('utf-8')

# Use the fernet_key for encryption and decryption
encryption_utils = EncryptionUtils(fernet_key)

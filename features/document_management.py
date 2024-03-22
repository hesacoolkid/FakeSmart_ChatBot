import os
from google.cloud import storage


class DocumentHandler:

  def __init__(self, bucket_name):
    if not bucket_name:
      raise ValueError("Bucket name is required for document handling.")

    self.bucket_name = bucket_name
    self.storage_client = storage.Client()
    self.bucket = self.storage_client.bucket(bucket_name)

  def upload_document(self, file_stream, file_name, content_type):
    if not file_stream or not file_name or not content_type:
      raise ValueError(
          "File stream, name, and content type are required for uploading.")

    try:
      blob = self.bucket.blob(file_name)
      blob.upload_from_string(file_stream, content_type=content_type)
      return blob.public_url
    except Exception as e:
      print(f"Failed to upload document: {e}")
      return None

  def retrieve_document(self, file_name):
    if not file_name:
      raise ValueError("File name is required for retrieving a document.")

    try:
      blob = self.bucket.blob(file_name)
      if blob.exists():
        return blob.download_as_bytes()
      else:
        print(f"Document {file_name} does not exist.")
        return None
    except Exception as e:
      print(f"Failed to retrieve document: {e}")
      return None

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import EMAIL_SERVICE_API_KEY

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Standard SMTP port
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email address


def send_email(recipient_email, subject, body):
  """
    Sends an email to the specified recipient.

    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
  # Create a multipart message and set headers
  message = MIMEMultipart()
  message['From'] = EMAIL_ADDRESS
  message['To'] = recipient_email
  message['Subject'] = subject

  # Add body to the email
  message.attach(MIMEText(body, 'plain'))

  # Connect to the SMTP server
  with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure the connection
    if EMAIL_SERVICE_API_KEY is not None:
      server.login(EMAIL_ADDRESS, EMAIL_SERVICE_API_KEY)
    else:
      # Handle the case where EMAIL_SERVICE_API_KEY is None
      pass  # Login with your email service API key or password
    server.send_message(message)  # Send the email

    print(f"Email sent to {recipient_email}")

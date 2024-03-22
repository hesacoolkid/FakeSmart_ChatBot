import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import (
    EMAIL_ADDRESS,
    EMAIL_SERVICE_API_KEY,
    SMTP_PORT,
    SMTP_SERVER,
)

class EmailIntegration:

  def __init__(self):
    self.smtp_server = SMTP_SERVER
    self.smtp_port = SMTP_PORT
    self.email_address = EMAIL_ADDRESS
    self.email_password = EMAIL_SERVICE_API_KEY

  def send_email(self, recipient, subject, body):
    if not recipient or not subject or not body:
      raise ValueError(
          "Recipient, subject, and body are required to send an email.")

    message = MIMEMultipart()
    message['From'] = self.email_address
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
      server = smtplib.SMTP(self.smtp_server, self.smtp_port)
      server.starttls()
      server.login(self.email_address, self.email_password)
      server.sendmail(self.email_address, recipient, message.as_string())
      server.quit()
      print(f"Email sent successfully to {recipient}.")
    except Exception as e:
      print(f"Failed to send email to {recipient}: {e}")

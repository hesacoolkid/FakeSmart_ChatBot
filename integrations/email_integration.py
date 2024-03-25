import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import (
    SMTP_SERVER,
    SMTP_PORT,
)

class EmailIntegration:

  def __init__(self, app.config):
    self.smtp_server = app.config.get('SMTP_SERVER')
    self.smtp_port = app.config.get('SMTP_PORT')
    self.client_email_address = app.config.get('CLIENT_EMAIL_ADDRESS')
    self.client_email_password = app.config.get('CLIENT_EMAIL_PASSWORD')

  def send_email(self, recipient, subject, body):
    if not recipient or not subject or not body:
      raise ValueError(
          "Recipient, subject, and body are required to send an email.")

    message = MIMEMultipart()
    message['From'] = self.client_email_address
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
      server = smtplib.SMTP(self.smtp_server, self.smtp_port)
      server.starttls()
      server.login(self.client_email_address, self.client_email_password)
      server.sendmail(self.client_email_address, recipient, message.as_string())
      server.quit()
      print(f"Email sent successfully to {recipient}.")
    except Exception as e:
      print(f"Failed to send email to {recipient}: {e}")
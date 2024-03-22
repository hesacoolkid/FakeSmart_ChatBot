from email_utils import send_email


class FollowUpManager:

  def __init__(self, email_sender):
    self.email_sender = email_sender

  def send_follow_up_email(self, customer_id, email_address, subject, message):
    if not all([email_address, subject, message]):
      raise ValueError(
          "Email address, subject, and message are required for sending follow-up email."
      )

    try:
      # Call the email sending function
      self.email_sender.send_email(email_address, subject, message)
      success_msg = f"Follow-up email sent to {email_address} for customer {customer_id}."
      print(success_msg)
    except Exception as e:
      error_msg = f"Error sending follow-up email to {email_address}: {e}"
      print(error_msg)

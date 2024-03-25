from integrations.email_integration import EmailIntegration

class FollowUpManager:
    def __init__(self, email_integration: EmailIntegration):
        self.email_integration = email_integration

    def send_follow_up(self, customer_id, email_address):
        """
        Send a follow-up message to the customer's email.

        Args:
            customer_id (str): The customer's unique identifier.
            email_address (str): The email address of the customer.
        """
        if not customer_id or not email_address:
            raise ValueError("Customer ID and email address are required for sending follow-up emails.")

        subject = "Thank you for your interaction"
        body = f"Hello, this is a follow-up to your recent interaction. Your customer ID is {customer_id}."

        # Use the EmailIntegration service to send the email
        self.email_integration.send_email(email_address, subject, body)

import chat_handler
import email_utils
import functions
import os
import openai
from app.config import OPENAI_API_KEY, ENABLE_DOCUMENT_UPLOAD
from email_integrations import EmailIntegration
from flask import Flask, request, jsonify
from utilities.hashing_utils import generate_customer_id


# Set the OpenAI API key from the config
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)
email_integration = EmailIntegration()

@app.route('/start', methods=['GET'])
def start_conversation():
  if ENABLE_DOCUMENT_UPLOAD:
    print("Document upload feature is enabled.")
  return jsonify({
      "message":
      "Conversation started. Please send your message to /chat endpoint."
  })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON or mimetype"}), 400

    user_input = data.get('message', '')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Use the handle_chat function from chat_handler to process the input
    response = chat_handler.handle_chat(user_input)
    return jsonify({"response": response})

@app.route('/identify', methods=['POST'])
def identify_user():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON or mimetype"}), 400

    user_info = data.get('email')  # or phone number, etc.
    if not user_info:
        return jsonify({"error": "Missing user information"}), 400

    customer_id = generate_customer_id(user_info)
    return jsonify({"customer_id": customer_id})


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)


@app.route('/send-follow-up', methods=['POST'])
def send_follow_up_email():
    data = request.json
    recipient_email = data.get('email')
    subject = "Your Recent Chat Session"
    body = "Here is a summary of your chat session..."

    # Use the send_email method from the EmailIntegration instance
    email_integration.send_email(recipient_email, subject, body)

    return jsonify({"message": "Follow-up email sent successfully."})

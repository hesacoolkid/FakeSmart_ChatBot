from flask import Flask, request, jsonify
from google.cloud import firestore
from app.config import OPENAI_API_KEY, ENABLE_DOCUMENT_UPLOAD
from utilities.hashing_utils import generate_customer_id
from app.chat_handler import handle_chat
from integrations.email_integration import EmailIntegration
from app.user_management import identify_user, update_user_interaction
from utilities.encryption_utils import EncryptionUtils
from flask import Flask
import os

app = Flask(__name__)
app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
db = firestore.Client()

if not app.config['OPENAI_API_KEY']:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Initialize EmailIntegration
email_integration = EmailIntegration()

# Initialize EncryptionUtils with a key (ensure this key is securely managed)
encryption_key = b'your_encryption_key_here'  # This should be a securely generated key
encryption_utils = EncryptionUtils(encryption_key)

def get_or_create_user(email):
    users_ref = db.collection('users')
    query_ref = users_ref.where('email', '==', email).limit(1)
    docs = query_ref.stream()

    user = next(docs, None)
    if user:
        return user.to_dict()  # User exists, return their data
    else:
        # User does not exist, create new user record
        user_ref = users_ref.document()
        user_data = {
            'email': email,
            'created_at': firestore.SERVER_TIMESTAMP,
            # Add other necessary fields as needed
        }
        user_ref.set(user_data)
        return user_data  # Return the new user data

@app.route('/start', methods=['GET'])
def start_conversation():
    if ENABLE_DOCUMENT_UPLOAD:
        print("Document upload feature is enabled.")
    return jsonify({"message": "Conversation started. Please send your message to /chat endpoint."})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid JSON or missing 'message' field"}), 400

    user_input = data.get('message', '')
    response = handle_chat(user_input)
    return jsonify({"response": response})

@app.route('/identify', methods=['POST'])
def identify_user():
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    user_data = get_or_create_user(email)
    return jsonify(user_data), 200


@app.route('/identify', methods=['POST'])
def identify():
    data = request.json
    if not data or 'email' not in data:
        return jsonify({"error": "Invalid JSON or missing 'email' field"}), 400

    user_email = data['email']
    customer_id = identify_user(user_email)
    if customer_id:
        return jsonify({"customer_id": customer_id})
    else:
        return jsonify({"error": "Could not identify user"}), 400
    
@app.route('/send-follow-up', methods=['POST'])
def send_follow_up_email():
    data = request.json
    if not data or 'email' not in data:
        return jsonify({"error": "Invalid JSON or missing 'email' field"}), 400

    recipient_email = data['email']
    subject = "Your Recent Chat Session"
    body = "Here is a summary of your chat session..."

    # Use the send_email method from the EmailIntegration instance
    result = email_integration.send_email(recipient_email, subject, body)
    if result:
        return jsonify({"message": "Follow-up email sent successfully."})
    else:
        return jsonify({"error": "Failed to send follow-up email"}), 500

# Add more routes as needed based on your application requirements

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
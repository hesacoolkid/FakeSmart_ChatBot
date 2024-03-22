import os

# General Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Feature toggles
ENABLE_DOCUMENT_UPLOAD = os.getenv('ENABLE_DOCUMENT_UPLOAD',
                                   'no').lower() == 'yes'
ENABLE_PRODUCT_RECOMMENDATION = os.getenv('ENABLE_PRODUCT_RECOMMENDATION',
                                          'no').lower() == 'yes'
ENABLE_APPOINTMENT_SCHEDULING = os.getenv('ENABLE_APPOINTMENT_SCHEDULING',
                                          'no').lower() == 'yes'
ENABLE_FOLLOW_UPS = os.getenv('ENABLE_FOLLOW_UPS', 'no').lower() == 'yes'
ENABLE_INVENTORY_MANAGEMENT = os.getenv('ENABLE_INVENTORY_MANAGEMENT',
                                        'no').lower() == 'yes'
ENABLE_FEEDBACK_COLLECTION = os.getenv('ENABLE_FEEDBACK_COLLECTION',
                                       'no').lower() == 'yes'

# Integration-specific configurations
CRM_API_KEY = os.getenv('CRM_API_KEY')
EMAIL_SERVICE_API_KEY = os.getenv('EMAIL_SERVICE_API_KEY')

# Fine-tuned model identifier for GPT-4 if applicable
CUSTOM_GPT4_MODEL_ID = os.getenv('CUSTOM_GPT4_MODEL_ID')

# Add other configuration parameters as needed

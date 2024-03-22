import os
import openai

# Set the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_chatgpt_response(user_input):
  """
    Sends user input to the ChatGPT model and retrieves the response.

    Args:
        user_input (str): The message from the user.

    Returns:
        str: The response from the ChatGPT model.
    """
  response = openai.Completion.create(
      model="gpt-4-1106-preview",  # Using the specified GPT-4 model
      prompt=user_input,
      max_tokens=500  # Adjust based on your needs
  )

  # Extracting the text response from the completion
  return response.choices[0].text.strip()


def handle_chat(user_input):
  """
    Main function to handle the chat interaction.

    Args:
        user_input (str): The message from the user.

    Returns:
        str: The response message from the ChatGPT model.
    """
  return get_chatgpt_response(user_input)

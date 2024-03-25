from openai import OpenAI
from flask import current_app

def get_chatgpt_response(user_input):
    """
    Communicates with OpenAI's API to get a response for the user's input using the streaming API.

    Args:
        user_input (str): The message from the user.

    Returns:
        str: The response from the ChatGPT model.
    """
    client = OpenAI(api_key=current_app.config['OPENAI_API_KEY'])

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}],
        stream=True,
    )

    response_content = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_content += chunk.choices[0].delta.content

    return response_content

def handle_chat(user_input):
    """
    Processes user input and returns the chatbot's response.

    Args:
        user_input (str): Input message from the user.

    Returns:
        str: Chatbot's response.
    """
    return get_chatgpt_response(user_input)

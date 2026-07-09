from ollama import chat

import config
import memory

def get_response():

    response = chat(
        model=config.MODEL_NAME,
        messages=memory.get_messages()
    )
    return response["message"]["content"]
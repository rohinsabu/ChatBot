from ollama import chat

import config
import prompts


def generate_response(messages, stream=True):

    conversation = [
        {
            "role": "system",
            "content": prompts.SYSTEM_PROMPT
        }
    ]

    conversation.extend(messages)

    response = chat(
        model=config.MODEL_NAME,
        messages=conversation,
        stream=stream
    )

    if stream:

        full_response = ""

        for chunk in response:
            
            content = chunk["message"]["content"]
            full_response += content

        return full_response

    return response["message"]["content"]
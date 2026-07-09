from ollama import chat

import config
import memory
import prompts


def get_response():

    messages = [
        {
            "role": "system",
            "content": prompts.SYSTEM_PROMPT
        }
    ]

    messages.extend(memory.get_messages())

    response = chat(
        model=config.MODEL_NAME,
        messages=messages,
        stream=True
    )

    full_response = ""

    print("Bot: ", end="")

    for chunk in response:

        content = chunk["message"]["content"]

        print(content, end="", flush=True)

        full_response += content

    print()

    return full_response
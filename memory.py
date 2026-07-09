# Stores the entire conversation
messages = []


def add_user_message(message):
    messages.append
    (
        {
            "role": "user",
            "content": message
        }
    )

def add_assistant_message(message):
    messages.append
    (
        {
            "role": "assistant",
            "content": message
        }
    )

def get_messages():
    return messages


def clear_memory():
    messages.clear()
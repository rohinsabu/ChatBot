from ollama import chat
import config
print(config.WELCOME_MESSAGE)
print("Type 'exit' to quit.\n")

# Store the entire conversation
messages = []

while True:

    user_input = input("You: ")

    if user_input.lower() == config.EXIT_COMMAND:
        print(config.GOODBYE_MESSAGE)
        break

    # Save the user's message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send the entire conversation
    response = chat(
        model=config.MODEL_NAME,
        messages=messages
    )

    bot_reply = response["message"]["content"]

    print("Bot:", bot_reply)

    # Save the bot's reply
    messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )
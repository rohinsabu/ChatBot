from ollama import chat
import config
import memory
print(config.WELCOME_MESSAGE)
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == config.EXIT_COMMAND:
        print(config.GOODBYE_MESSAGE)
        break

    memory.add_user_message(user_input)

    # Send the entire conversation
    response = chat(
        model=config.MODEL_NAME,
        messages=memory.get_messages()
    )

    bot_reply = response["message"]["content"]

    print("Bot:", bot_reply)

    memory.add_assistant_message(bot_reply)
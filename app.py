from ollama import chat
import config
import memory
import chatbot

print(config.WELCOME_MESSAGE)
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == config.EXIT_COMMAND:
        print(config.GOODBYE_MESSAGE)
        break

    memory.add_user_message(user_input)

    bot_reply = chatbot.get_response()

    print("Bot:", bot_reply)

    memory.add_assistant_message(bot_reply)
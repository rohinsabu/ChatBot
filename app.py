from ollama import chat
import config
import memory
import chatbot
import commands

print(config.WELCOME_MESSAGE)
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if commands.handle_command(user_input):
        continue
    if user_input.lower() == config.EXIT_COMMAND:
        print("Bot: Goodbye!")
        break

    memory.add_user_message(user_input)

    bot_reply = chatbot.generate_response(memory.get_messages())

    memory.add_assistant_message(bot_reply)
    
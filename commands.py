import os
from datetime import datetime
from pyexpat.errors import messages

import memory
import config

def handle_command(command):

    if command == "/help":

        print("""
═══════════════════════════════════════
           Available Commands
═══════════════════════════════════════

/help      Show all available commands
/clear     Clear conversation memory
/history   Show conversation history
/save      Save conversation to a file
/model     Show current AI model
/about     About this chatbot
/exit      Exit the chatbot

═══════════════════════════════════════
""")

        return True

    elif command == "/clear":

        confirm = input("Are you sure you want to clear the conversation? (y/n): ")

        if confirm.lower() == "y":
            memory.clear_memory()
            print("✅ Conversation memory cleared.")
        else:
            print("Conversation was not cleared.")

        return True

    elif command == "/model":

        print(f"Current AI model: {config.MODEL_NAME}")

        return True

    elif command == "/history":

        messages = memory.get_messages()

        if not messages:
            print("No conversation history available.")
            return True

        print("""
═══════════════════════════════════════
         Conversation History
═══════════════════════════════════════
""")

        for message in messages:

            if message["role"] == "user":
                print(f"👤 User: {message['content']}\n")

            elif message["role"] == "assistant":
                print(f"🤖 Ronin: {message['content']}\n")


    elif command == "/save":
        messages = memory.get_messages()
        messages = memory.get_messages()

        if not messages:
            print("⚠️ No conversation to save.")
            return True
        
        # Create the exports folder if it doesn't exist
        os.makedirs("exports", exist_ok=True)

        # Create a unique filename using the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"exports/chat_{timestamp}.txt"

        # Write the conversation to the file
        with open(filename, "w", encoding="utf-8") as file:

            file.write("═══════════════════════════════════════\n")
            file.write("        Ronin AI Chat Export\n")
            file.write("═══════════════════════════════════════\n\n")

            for message in memory.get_messages():

                if message["role"] == "user":
                    file.write(f"👤 User: {message['content']}\n\n")

                elif message["role"] == "assistant":
                    file.write(f"🤖 Ronin: {message['content']}\n\n")

        print(f"✅ Conversation saved successfully!")
        print(f"📁 File location: {filename}")

        return True
        

    return False
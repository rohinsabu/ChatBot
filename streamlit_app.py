import streamlit as st
import chatbot

st.set_page_config(
    page_title="Ronin AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Ronin AI")
st.subheader("Powered by Ollama")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    bot_reply = chatbot.generate_response(
        st.session_state.messages,
        stream=False
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )
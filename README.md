# 🤖 Ronin AI

Ronin AI is a local AI chatbot built with **Python**, **Ollama**, and **Streamlit**. It runs completely offline using the **Llama 3.2** language model and provides both a command-line interface (CLI) and a modern web interface.

The project is designed with a modular architecture, making it easy to extend with features such as Retrieval-Augmented Generation (RAG), databases, and machine learning models.

---

# Features

- 🧠 Local AI chatbot powered by Ollama
- 💬 Conversation memory
- ⚡ Real-time response generation
- 🎯 Configurable system prompts
- 🌐 Streamlit web interface
- 💻 Command-line interface (CLI)
- 📂 Export conversations to text files
- 🏗️ Modular project architecture
- 🔌 Easy to extend with RAG and Machine Learning

---

# Software Requirements

- Python 3.12+
- Visual Studio Code
- Ollama
- Git (optional)

---

# Technologies Used

- Python 3.12
- Ollama
- Llama 3.2
- Streamlit
- Visual Studio Code

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd ChatBot
```

Or download the project as a ZIP file.

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

---

## 5. Download the Llama Model

```bash
ollama pull llama3.2
```

---

# Running the Application

## Command Line Version

```bash
python app.py
```

---

## Streamlit Web Interface

```bash
python -m streamlit run streamlit_app.py
```

The application will open in your browser.

---

# Project Structure

```text
ChatBot/
│
├── app.py                  # Command-line interface
├── streamlit_app.py        # Streamlit web application
├── chatbot.py              # AI response generation
├── memory.py               # CLI conversation memory
├── commands.py             # CLI command handling
├── prompts.py              # System prompt configuration
├── config.py               # Application configuration
├── exports/                # Saved conversations
├── requirements.txt
├── README.md
└── venv/
```

---

# Available CLI Commands

| Command    | Description                   |
| ---------- | ----------------------------- |
| `/help`    | Display available commands    |
| `/clear`   | Clear conversation memory     |
| `/history` | Show conversation history     |
| `/model`   | Display the current AI model  |
| `/save`    | Save the current conversation |
| `exit`     | Exit the chatbot              |

---

# Application Architecture

```text
                     Ronin AI
                          │
            ┌─────────────┴─────────────┐
            │                           │
     Command Line                 Streamlit UI
       (app.py)               (streamlit_app.py)
            │                           │
            └─────────────┬─────────────┘
                          │
                    chatbot.py
                          │
                System Prompt Engine
                          │
                 Ollama (Llama 3.2)
```

---

# Current Features

- Local AI chatbot
- Conversation memory
- System prompts
- Streaming-ready architecture
- Streamlit web interface
- Session-based chat history
- Conversation export
- Modular codebase

---

# Future Improvements

- 📄 Retrieval-Augmented Generation (RAG)
- 📚 PDF document support
- 🗄️ SQLite chat history
- 🧠 Machine Learning integration
- 😊 Sentiment analysis
- 🎯 Intent classification
- 🧩 Vector database (ChromaDB)
- 🌙 Enhanced Streamlit interface
- 🐳 Docker support
- ☁️ Cloud deployment

---

# Learning Objectives

This project was built to gain hands-on experience with:

- Python application development
- Modular software architecture
- Local Large Language Models (LLMs)
- Ollama
- Prompt engineering
- Conversation memory
- Streamlit
- AI chatbot development
- Preparing for Retrieval-Augmented Generation (RAG)

---

# Version

**Current Version:** `v1.0.0`

---

# License

This project is intended for educational and learning purpos

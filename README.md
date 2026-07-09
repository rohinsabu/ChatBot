# AI Chatbot using Python and Ollama

A modular command-line AI chatbot built using **Python** and **Ollama**. The chatbot runs locally using the **Llama 3.2** language model and provides a conversational AI experience with streaming responses, conversation memory, and configurable system prompts.

---

# Features

- Runs completely offline (no paid API required)
- Interactive command-line chatbot
- Built with Python and Ollama
- Conversation memory for contextual responses
- Real-time streaming responses
- Configurable AI personality using system prompts
- Modular project architecture
- Easy to extend with RAG, databases, and web interfaces

---

# Software Requirements

- Python 3.12 or later
- Visual Studio Code
- Ollama

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd ChatBot
```

Or download the project as a ZIP file and extract it.

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

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

## 5. Download the Llama 3.2 Model

```bash
ollama pull llama3.2
```

---

# Running the Chatbot

Start the chatbot:

```bash
python app.py
```

Type your message and press **Enter**.

To quit:

```text
exit
```

---

# Project Structure

```text
ChatBot/
│
├── app.py             # Main application loop
├── chatbot.py         # Handles communication with Ollama
├── memory.py          # Stores conversation history
├── prompts.py         # System prompt and AI personality
├── config.py          # Application configuration
├── requirements.txt
├── README.md
└── venv/
```

---

# Technologies Used

- Python 3.12
- Ollama
- Llama 3.2
- Visual Studio Code

---

# Current Architecture

```text
User
 │
 ▼
app.py
 │
 ├────────► memory.py
 │              │
 │              ▼
 │      Conversation History
 │
 └────────► chatbot.py
                 │
                 ▼
            System Prompt
                 │
                 ▼
             Ollama (Llama 3.2)
                 │
                 ▼
              AI Response
```

---

# Current Features

- Interactive command-line interface
- Local LLM execution using Ollama
- Conversation memory
- Streaming AI responses
- Modular codebase
- Configurable system prompts

---

# Future Improvements

- Command system (`/help`, `/clear`, `/history`, `/save`)
- Chat history stored in SQLite
- Streamlit web interface
- PDF upload support
- Retrieval-Augmented Generation (RAG)
- Vector database integration (ChromaDB/FAISS)
- Multi-document search
- AI agent capabilities
- Docker deployment

---

# Learning Objectives

This project was built to understand the fundamentals of modern AI chatbot development, including:

- Python project structure
- Working with local LLMs
- Prompt engineering
- Conversation memory
- Streaming responses
- Modular software architecture
- Preparing for Retrieval-Augmented Generation (RAG)

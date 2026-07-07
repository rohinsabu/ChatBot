# AI Chatbot using Python and Ollama

A simple command-line AI chatbot built using Python and Ollama. The chatbot runs locally using the Llama 3.2 language model and allows users to interact with an AI assistant through the terminal.

## Features

- Local AI chatbot (no paid API required)
- Runs completely offline
- Interactive command-line interface
- Built using Python and Ollama
- Easy to extend with conversation memory and RAG

---

## Software Requirements

- Python 3.12 or later
- Visual Studio Code
- Ollama

---

## Installation

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd chatbot
```

Or download the project as a ZIP file and extract it.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
venv\Scripts\activate
```

### 3. Install Required Python Packages

```bash
python -m pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

### 5. Download the Llama 3.2 Model

```bash
ollama pull llama3.2
```

---

## Running the Chatbot

Start the chatbot using:

```bash
python app.py
```

Type your message and press Enter.

To exit the chatbot:

```text
exit
```

---

## Project Structure

```
chatbot/
│── app.py
│── README.md
│── requirements.txt
│── venv/
```

---

## Technologies Used

- Python 3.12
- Ollama
- Llama 3.2
- Visual Studio Code

---

## Future Improvements

- Conversation memory
- Streamlit web interface
- RAG (Retrieval-Augmented Generation)
- PDF document support
- Chat history

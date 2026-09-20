# Personal AI Agent with Long-Term Memory

This is a Python-based AI assistant powered by Google's Gemini API and ChromaDB. Unlike standard chatbots, this agent uses local vector storage to remember past conversations, facts, and context across different sessions.

## Features
- **Persistent Memory:** Uses ChromaDB to save and recall user inputs.
- **Context-Aware Responses:** Injects past memories into the Gemini system prompt for personalized answers.
- **Local Database:** Memory is stored securely on your local machine.

## Setup & Installation

If you want to run this agent on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone https://github.com/Ayush-vishwakarma417/Python-Project-AI-API.git
cd Python-Project-AI-API
```

**2. Install dependencies**
Run this exact command in your terminal to install the required tools:
```bash
pip install chromadb google-generativeai python-dotenv
```

**3. Add your API Key**
For security, the API key is not included in this repository. You must create your own `.env` file in the root folder and add your personal Google Gemini API key:
```text
GEMINI_API_KEY="your_personal_api_key_here"
```

**4. Run the Engine**
Start the assistant by running the main Python script:
```bash
python agent.py
```


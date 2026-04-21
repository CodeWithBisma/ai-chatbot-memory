# Mnemosyne · AI Chatbot with Persistent Memory

Mnemosyne is a context-aware AI chatbot built with Python and Flask. It features persistent memory, simple conversational intelligence, and a clean web interface. The system stores and retrieves conversation history to simulate continuity across sessions.

---

## Live Demo

https://ai-chatbot-memory-85ow.vercel.app/

You can interact with the chatbot directly in the browser. No installation is required.

---

## Features

- Persistent memory using JSON storage
- User name recognition and recall
- Context-aware responses using recent conversation history
- Basic sentiment-aware responses (rule-based)
- REST API endpoint for chat interaction
- Web-based chat interface
- Optional CLI mode for terminal usage

---

## Tech Stack

| Layer    | Technology            |
|----------|----------------------|
| Backend  | Python, Flask        |
| Frontend | HTML, CSS, JavaScript |
| Storage  | JSON file-based memory |

---

---

## How It Works

1. User sends a message via web UI or API
2. Backend processes input using rule-based AI logic
3. Memory service stores conversation in JSON format
4. System retrieves recent context for smarter responses
5. Response is returned to the frontend and displayed in chat UI

---

## API Reference

### POST `/chat`

Send a message to the chatbot.

**Request:**
```json
{
  "message": "My name is Ali"
}
{
  "response": "Nice to meet you, Ali! I will remember your name."
}

Future Improvements

Integration with large language models (OpenAI / Claude)
React-based frontend with real-time streaming responses
Cloud database for scalable memory storage
Authentication system for multiple users
Deployment with full production architecture
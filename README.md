# Mnemosyne · AI Chatbot with Persistent Memory

> A context-aware conversational AI built with Python and Flask, featuring persistent JSON-based memory, emotional intelligence, and a polished dark UI.

---

## Features

- **Persistent memory** — conversations survive server restarts via a local JSON store
- **Name recall** — remembers who you are across sessions
- **Context-awareness** — reads the last 3 turns to inform its response
- **Emotional intelligence** — detects sentiment in prior messages and responds empathetically
- **REST API** — clean `/chat` endpoint, health check at `/health`
- **CLI mode** — run `main.py` for a terminal interface with color output
- **Responsive UI** — works on desktop and mobile

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11 · Flask |
| Memory | JSON file store (no database required) |
| Frontend | HTML · CSS · Vanilla JS |
| Fonts | Sora · JetBrains Mono |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/mnemosyne-chatbot.git
cd mnemosyne-chatbot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the web app
python app.py
# → Open http://localhost:5000

# 5. Or use the CLI
python main.py
```

---

## Project Structure

```
mnemosyne-chatbot/
├── app.py              # Flask app & response logic
├── main.py             # CLI interface
├── chatbot/
│   └── memory.py       # JSON memory engine
├── templates/
│   └── index.html      # Chat UI
├── static/
│   └── style.css       # Styling
└── data/
    └── memory.json     # Auto-generated memory store
```

---

## API Reference

### `POST /chat`

**Request**
```json
{ "message": "My name is Alex" }
```

**Response**
```json
{ "response": "Nice to meet you, Alex! I'll remember that." }
```

### `GET /health`
```json
{ "status": "ok", "service": "Mnemosyne Chatbot" }
```

---

## Design Decisions

- **No database** — JSON keeps the project self-contained and easy to inspect/debug
- **Atomic writes** — memory is written via a `.tmp` file then renamed, preventing corruption
- **Graceful degradation** — corrupted or missing memory files are handled without crashing
- **Separation of concerns** — response logic in `app.py`, memory I/O isolated in `memory.py`

---

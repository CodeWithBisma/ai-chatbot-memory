"""
chatbot/memory.py — Persistent JSON Memory Store

Handles reading and writing conversation history and user metadata
to a local JSON file. Designed to be simple, portable, and transparent —
no external database dependencies required.
"""

import json
import os
from typing import Optional

# ── Configuration ──────────────────────────────────────────────────────────────
MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "memory.json")

_DEFAULT_STORE = {
    "name": None,
    "history": []
}


# ── Core I/O ───────────────────────────────────────────────────────────────────

def load_memory() -> dict:
    """Load the full memory store from disk. Returns defaults if file is missing or corrupt."""
    if not os.path.exists(MEMORY_FILE):
        _ensure_data_dir()
        return dict(_DEFAULT_STORE)
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure required keys exist even in legacy files
            data.setdefault("name", None)
            data.setdefault("history", [])
            return data
    except (json.JSONDecodeError, OSError):
        return dict(_DEFAULT_STORE)


def save_memory(data: dict) -> None:
    """Persist the memory store to disk atomically."""
    _ensure_data_dir()
    tmp_path = MEMORY_FILE + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, MEMORY_FILE)


def _ensure_data_dir() -> None:
    """Create the data directory if it doesn't exist."""
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)


# ── History ────────────────────────────────────────────────────────────────────

def add_to_memory(user_input: str, bot_response: str) -> None:
    """Append a user–bot exchange to the conversation history."""
    data = load_memory()
    data["history"].append({
        "user": user_input,
        "bot": bot_response
    })
    save_memory(data)


def get_last_conversations(n: int = 5) -> list[dict]:
    """Return the last `n` conversation turns from memory."""
    data = load_memory()
    return data["history"][-n:]


def clear_history() -> None:
    """Wipe the conversation history while preserving user metadata."""
    data = load_memory()
    data["history"] = []
    save_memory(data)


# ── User metadata ──────────────────────────────────────────────────────────────

def save_name(name: str) -> None:
    """Store the user's name in memory."""
    data = load_memory()
    data["name"] = name.strip().title()
    save_memory(data)


def get_name() -> Optional[str]:
    """Retrieve the stored user name, or None if not set."""
    return load_memory().get("name")
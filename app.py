"""
Mnemosyne — AI Chatbot with Persistent Memory
Flask backend · JSON memory store · Context-aware responses

Author: [Your Name]
Stack: Python · Flask · JSON
"""

from flask import Flask, render_template, request, jsonify
from chatbot.memory import add_to_memory, get_last_conversations, save_name, get_name

app = Flask(__name__)


def get_response(user_input: str) -> str:
    """
    Generate a context-aware response based on user input
    and prior conversation history stored in memory.
    """
    text = user_input.strip().lower()

    # ── Name registration ──────────────────────────────────────
    if "my name is" in text:
        name = text.split("my name is", 1)[-1].strip().title()
        save_name(name)
        return f"Nice to meet you, {name}! I'll remember that for our future conversations."

    # ── Name recall ────────────────────────────────────────────
    if any(phrase in text for phrase in ("what is my name", "what's my name", "do you know my name")):
        name = get_name()
        return f"Your name is {name}." if name else "I don't know your name yet — feel free to introduce yourself!"

    # ── History request ────────────────────────────────────────
    history = get_last_conversations(3)

    if any(word in text for word in ("history", "what did we talk", "last conversation", "previous")):
        if not history:
            return "We haven't talked about anything yet. This is our first conversation!"
        lines = "\n".join(f"• You: {item['user']}\n  Me: {item['bot']}" for item in history)
        return f"Here's a summary of our recent exchange:\n\n{lines}"

    # ── Emotion-aware context ──────────────────────────────────
    if history:
        last_user = history[-1]["user"].lower()
        if "sad" in last_user or "upset" in last_user or "bad" in last_user:
            return "I noticed you seemed a bit down earlier. How are you feeling now?"
        if "happy" in last_user or "great" in last_user or "excited" in last_user:
            return "You seemed to be in a great mood earlier! Hope it's carried through 😊"

    # ── Standard responses ─────────────────────────────────────
    if any(word in text for word in ("hello", "hi", "hey", "good morning", "good evening")):
        name = get_name()
        greeting = f"Hello, {name}!" if name else "Hello!"
        return f"{greeting} I'm Mnemosyne, your memory-enabled AI assistant. How can I help you today?"

    if any(word in text for word in ("bye", "goodbye", "see you", "take care")):
        return "Goodbye! Your conversation has been saved. See you next time 👋"

    if "who are you" in text or "what are you" in text:
        return (
            "I'm Mnemosyne — a context-aware chatbot built with Python and Flask. "
            "I can remember your name, recall past conversations, and respond with emotional intelligence. "
            "My memory is persisted in a local JSON store between sessions."
        )

    # ── Fallback ───────────────────────────────────────────────
    return "Interesting — tell me more. I'm learning from everything we discuss."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True)
    if not payload or not payload.get("message"):
        return jsonify({"error": "Invalid request"}), 400

    user_input = payload["message"].strip()
    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    response = get_response(user_input)
    add_to_memory(user_input, response)

    return jsonify({"response": response})


@app.route("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok", "service": "Mnemosyne Chatbot"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
"""
main.py — Mnemosyne CLI Interface

Run the chatbot directly in your terminal without Flask.
Useful for testing logic and demonstrating memory behavior
without a browser.

Usage:
    python main.py
"""

from chatbot.memory import add_to_memory, get_last_conversations, save_name, get_name


RESET = "\033[0m"
BOLD  = "\033[1m"
CYAN  = "\033[96m"
GREEN = "\033[92m"
DIM   = "\033[2m"
YELLOW = "\033[93m"


def get_response(user_input: str) -> str:
    """Return a context-aware response based on user input and stored memory."""
    text = user_input.strip().lower()

    # ── Name registration ──────────────────────────────────────
    if "my name is" in text:
        name = text.split("my name is", 1)[-1].strip().title()
        save_name(name)
        return f"Nice to meet you, {name}! I'll remember your name."

    # ── Name recall ────────────────────────────────────────────
    if any(p in text for p in ("what is my name", "what's my name", "do you know my name")):
        name = get_name()
        return f"Your name is {name}." if name else "I don't know your name yet."

    # ── Context from prior turns ───────────────────────────────
    history = get_last_conversations(3)

    if history:
        last = history[-1]["user"].lower()
        if any(w in last for w in ("sad", "upset", "bad")):
            return "I noticed you seemed down earlier — are you feeling any better?"
        if any(w in last for w in ("happy", "great", "excited")):
            return "You seemed in a great mood earlier! Hope it's still going well 😊"

    # ── History request ────────────────────────────────────────
    if any(w in text for w in ("history", "last conversation", "what did we talk")):
        if not history:
            return "No previous conversations found."
        lines = "\n".join(f"  You: {h['user']}\n  Me:  {h['bot']}" for h in history)
        return f"Here's our recent exchange:\n\n{lines}"

    # ── Standard responses ─────────────────────────────────────
    if any(w in text for w in ("hello", "hi", "hey")):
        name = get_name()
        return f"Hello{', ' + name if name else ''}! I'm Mnemosyne, your memory-enabled assistant 😊"

    if any(w in text for w in ("bye", "goodbye", "exit")):
        return "Goodbye! Your conversation has been saved. See you next time."

    return "Interesting — tell me more. I'm learning from everything we discuss."


def chat():
    print(f"\n{BOLD}{CYAN}  Mnemosyne · AI Chatbot with Memory{RESET}")
    print(f"{DIM}  Type 'bye' to exit · 'history' to review past turns{RESET}\n")
    print(f"{DIM}{'─' * 45}{RESET}\n")

    while True:
        try:
            user_input = input(f"{YELLOW}  You › {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{DIM}  Session ended.{RESET}\n")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"\n{GREEN}  Bot › {RESET}{response}\n")

        add_to_memory(user_input, response)

        if any(w in user_input.lower() for w in ("bye", "goodbye", "exit")):
            break

    print(f"{DIM}  Memory saved. Goodbye!{RESET}\n")


if __name__ == "__main__":
    chat()
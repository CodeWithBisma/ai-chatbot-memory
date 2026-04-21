from chatbot.memory import add_to_memory
from chatbot.memory import get_last_conversations
from chatbot.memory import save_name, get_name
from chatbot.memory import get_last_conversations


def get_response(user_input):
    user_input_lower = user_input.lower()

    # 🧠 NAME MEMORY
    if "my name is" in user_input_lower:
        name = user_input_lower.replace("my name is", "").strip()
        save_name(name)
        return f"Nice to meet you {name}! I will remember your name."

    if "what is my name" in user_input_lower:
        name = get_name()
        if name:
            return f"Your name is {name}."
        else:
            return "I don’t know your name yet."

    # 🧠 CONTEXT-AWARE RESPONSE
    history = get_last_conversations(3)

    if history:
        last_user_message = history[-1]["user"].lower()

        if "sad" in last_user_message:
            return "I noticed you seemed sad earlier. Are you feeling okay?"

        if "happy" in last_user_message:
            return "You seemed happy earlier 😊 What made your day good?"

    # 🧠 HISTORY REQUEST
    if "history" in user_input_lower or "last" in user_input_lower:
        if not history:
            return "No previous conversations found."

        response = "Here’s what we talked about:\n"
        for item in history:
            response += f"- You: {item['user']} | Bot: {item['bot']}\n"
        return response

    # 💬 NORMAL RESPONSES
    if "hello" in user_input_lower:
        return "Hi! I can now understand context from our past chats 😊"

    elif "bye" in user_input_lower:
        return "Goodbye! I’ll remember our conversation."

    return "Tell me more. I'm learning from what you say."



def chat():
    print("Chatbot with Memory is running...\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        # SAVE MEMORY
        add_to_memory(user_input, response)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    chat()

from chatbot.memory import add_to_memory
from chatbot.memory import get_last_conversations
from chatbot.memory import save_name, get_name

def get_response(user_input):
    user_input_lower = user_input.lower()

    # SAVE NAME
    if "my name is" in user_input_lower:
        name = user_input_lower.replace("my name is", "").strip()
        save_name(name)
        return f"Nice to meet you {name}! I will remember your name."

    # ASK NAME
    if "what is my name" in user_input_lower:
        name = get_name()
        if name:
            return f"Your name is {name}."
        else:
            return "I don’t know your name yet. Tell me: My name is ..."

    if "hello" in user_input_lower:
        return "Hi! I can now remember your name"

    elif "bye" in user_input_lower:
        return "Goodbye!"

    else:
        return "Tell me something like your name or ask me questions."


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

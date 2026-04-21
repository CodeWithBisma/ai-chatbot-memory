from flask import Flask, render_template, request, jsonify
from chatbot.memory import add_to_memory, get_last_conversations, save_name, get_name

app = Flask(__name__)


def get_response(user_input):
    user_input_lower = user_input.lower()

    if "my name is" in user_input_lower:
        name = user_input_lower.replace("my name is", "").strip()
        save_name(name)
        return f"Nice to meet you {name}!"

    if "what is my name" in user_input_lower:
        name = get_name()
        return f"Your name is {name}." if name else "I don’t know your name yet."

    history = get_last_conversations(3)

    if history:
        last = history[-1]["user"].lower()
        if "sad" in last:
            return "You seemed sad earlier. Are you okay?"

    if "hello" in user_input_lower:
        return "Hi! I'm your AI chatbot 😊"

    return "Tell me more."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)

    add_to_memory(user_input, response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)

import json
import os

MEMORY_FILE = "data/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"history": []}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_to_memory(user_input, bot_response):
    data = load_memory()

    data["history"].append({
        "user": user_input,
        "bot": bot_response
    })

    save_memory(data)


def get_last_conversations(n=5):
    data = load_memory()
    return data["history"][-n:]

def get_last_conversations(n=5):
    data = load_memory()
    return data["history"][-n:]

def save_name(name):
    data = load_memory()
    data["name"] = name
    save_memory(data)


def get_name():
    data = load_memory()
    return data.get("name")

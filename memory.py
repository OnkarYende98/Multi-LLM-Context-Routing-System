import json

CHAT_HISTORY_FILE = "chat_history.json"


def load_history():

    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_history(history):

    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def add_message(role, content):

    history = load_history()

    history.append({
        "role": role,
        "content": content
    })

    save_history(history)


def clear_history():

    save_history([])
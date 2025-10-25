import json
import os

HISTORY_FILE = "modules/history.json"

def add_to_history(command, response):
    history_data = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history_data = json.load(f)
    history_data.append({"command": command, "response": response})
    with open(HISTORY_FILE, "w") as f:
        json.dump(history_data, f, indent=4)

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

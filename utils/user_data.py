import json
import os

DATA_FILE = "data/users.json"

def save_user(user):
    if not os.path.exists("data"):
        os.makedirs("data")

    users = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []

    users.append(user)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

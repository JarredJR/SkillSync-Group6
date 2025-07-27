import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "users.json")

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_user(new_user):
    users = load_users()
    users.append(new_user)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def validate_user(email, password):
    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            return user
    return None

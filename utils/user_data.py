import json
import os
from utils.path_helper import resource_path

USERS_FILE = resource_path("data/users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_user(new_user):
    users = load_users()
    users.append(new_user)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def validate_user(email, password):
    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            return user
    return None

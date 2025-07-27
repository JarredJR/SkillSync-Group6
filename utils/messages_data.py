import json
import os
from datetime import datetime
from utils.path_helper import resource_path

MESSAGES_FILE = resource_path("data/messages.json")

def _load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    try:
        with open(MESSAGES_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _save_messages(msgs):
    with open(MESSAGES_FILE, "w") as f:
        json.dump(msgs, f, indent=4)

def append_message(from_email: str, to_email: str, message: str):
    msgs = _load_messages()
    msgs.append({
        "from": from_email,
        "to": to_email,
        "message": message,
        "timestamp": datetime.now().isoformat(timespec="seconds")
    })
    _save_messages(msgs)

def get_conversation_partners(user_email: str):
    msgs = _load_messages()
    partners = set()
    for m in msgs:
        if m["from"] == user_email:
            partners.add(m["to"])
        if m["to"] == user_email:
            partners.add(m["from"])
    return sorted(list(partners))

def get_thread(user_email: str, partner_email: str):
    msgs = _load_messages()
    thread = [m for m in msgs if (m["from"] == user_email and m["to"] == partner_email) or
                                   (m["from"] == partner_email and m["to"] == user_email)]
    thread.sort(key=lambda m: m["timestamp"])
    return thread

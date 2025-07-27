import flet as ft
import json
import os
from utils.path_helper import resource_path

USERS_FILE = resource_path("users.json")

def signup_view(page: ft.Page):
    email = ft.TextField(label="Email", width=300)
    username = ft.TextField(label="Username", width=300)
    birthday = ft.TextField(label="Birthday", width=300)
    password = ft.TextField(label="Password", password=True, width=300)
    message = ft.Text()

    def register_user(e):
        user = {
            "email": email.value,
            "username": username.value,
            "birthday": birthday.value,
            "password": password.value
        }

        users = []
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []

        users.append(user)
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

        page.session.set("user", user)
        page.go("/role_question")

    return ft.View(
        "/signup",
        [
            ft.Text("Sign Up", size=30),
            email,
            username,
            birthday,
            password,
            ft.ElevatedButton("Register", on_click=register_user),
            ft.TextButton("Already have an account? Login", on_click=lambda _: page.go("/")),
            message
        ]
    )

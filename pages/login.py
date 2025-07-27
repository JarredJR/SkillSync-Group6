import flet as ft
import json
import os
from utils.path_helper import resource_path

def login_view(page: ft.Page):
    users_path = resource_path("users.json")
    if not os.path.exists(users_path):
        os.makedirs(os.path.dirname(users_path), exist_ok=True)
        with open(users_path, "w") as f:
            json.dump([], f)

    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, width=300)
    status = ft.Text(color="red")

    def login_action(e):
        with open(users_path, "r") as f:
            users = json.load(f)
        user = next((u for u in users if u["email"] == email.value and u["password"] == password.value), None)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            status.value = "Invalid email or password"
            page.update()

    return ft.View(
        "/login",
        [
            ft.Column(
                [
                    ft.Text("Login", size=30, weight="bold"),
                    email,
                    password,
                    ft.ElevatedButton("Login", on_click=login_action),
                    ft.TextButton("Don't have an account? Sign Up", on_click=lambda e: page.go("/signup")),
                    status
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )

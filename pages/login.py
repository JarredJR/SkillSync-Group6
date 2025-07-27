import flet as ft
import json
import os

def login_view(page: ft.Page):
    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, width=300)
    error_msg = ft.Text(color="red")

    def login_user(e):
        users_path = os.path.join("data", "users.json")
        if not os.path.exists(users_path):
            error_msg.value = "User database not found."
            page.update()
            return

        with open(users_path, "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []

        for user in users:
            if user.get("email") == email.value and user.get("password") == password.value:
                page.session.set("user", user)  
                page.go("/dashboard")
                return

        error_msg.value = "Invalid credentials"
        page.update()

    return ft.View(
        "/login",
        controls=[
            ft.AppBar(title=ft.Text("Login")),
            ft.Column(
                [
                    email,
                    password,
                    ft.ElevatedButton("Login", on_click=login_user),
                    ft.TextButton("Don't have an account? Sign up", on_click=lambda e: page.go("/signup")),
                    error_msg
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=20
            )
        ],
        scroll=ft.ScrollMode.AUTO
    )

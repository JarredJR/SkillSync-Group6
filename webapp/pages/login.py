import flet as ft

def LoginPage():
    return ft.Column(
        controls=[
            ft.Text("Login to SkillSync", size=30, weight="bold"),
            ft.TextField(label="Username"),
            ft.TextField(label="Password", password=True, can_reveal_password=True),
            ft.ElevatedButton("Login")
        ],
        horizontal_alignment="center"
    )

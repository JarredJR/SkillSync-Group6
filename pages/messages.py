import flet as ft
from utils.messages_data import get_conversation_partners
from utils.user_data import load_users
from components.topbar import topbar

def messages_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return

    partners_col = ft.Column(spacing=10, expand=True)

    def open_chat_with(email):
        page.session.set("chat_with", email)
        page.go("/chat")

    def email_to_username(email):
        for u in load_users():
            if u["email"] == email:
                return u.get("username", email)
        return email

    def load_partners():
        partners_col.controls.clear()
        partners = get_conversation_partners(user["email"])
        if not partners:
            partners_col.controls.append(ft.Text("No conversations yet."))
        else:
            for p in partners:
                partners_col.controls.append(
                    ft.ListTile(
                        title=ft.Text(email_to_username(p)),
                        subtitle=ft.Text(p),
                        on_click=lambda e, p=p: open_chat_with(p)
                    )
                )
        page.update()

    load_partners()

    return ft.View(
        "/messages",
        controls=[
            topbar(page, "Messages"),
            ft.Container(content=partners_col, padding=20)
        ]
    )

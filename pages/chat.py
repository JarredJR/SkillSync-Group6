import flet as ft
from utils.messages_data import get_thread, append_message
from utils.user_data import load_users
from components.topbar import topbar

def chat_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return

    partner_email = page.session.get("chat_with")
    if not partner_email:
        page.go("/messages")
        return

    def email_to_username(email):
        for u in load_users():
            if u["email"] == email:
                return u.get("username", email)
        return email

    partner_username = email_to_username(partner_email)
    msg_list = ft.Column(spacing=10, scroll=ft.ScrollMode.ALWAYS, expand=True)
    message_input = ft.TextField(hint_text=f"Message {partner_username}...", expand=True, multiline=False)

    def load_thread():
        msg_list.controls.clear()
        thread = get_thread(user["email"], partner_email)
        if not thread:
            msg_list.controls.append(ft.Text("No messages yet. Say hi!"))
        else:
            for m in thread:
                is_me = m["from"] == user["email"]
                bubble = ft.Container(
                    content=ft.Column([
                        ft.Text(m["message"]),
                        ft.Text(m["timestamp"], size=10, color="#777777")
                    ], tight=True),
                    bgcolor="#DCF8C6" if is_me else "#FFFFFF",
                    padding=10,
                    border_radius=10,
                    margin=ft.margin.only(left=50) if is_me else ft.margin.only(right=50),
                    alignment=ft.alignment.center_right if is_me else ft.alignment.center_left
                )
                msg_list.controls.append(bubble)
        page.update()

    def send_message(e):
        text = message_input.value.strip()
        if not text:
            return
        append_message(user["email"], partner_email, text)
        message_input.value = ""
        load_thread()

    load_thread()

    return ft.View(
        "/chat",
        controls=[
            topbar(page, f"Chat with {partner_username}"),
            ft.Container(content=msg_list, expand=True, padding=10),
            ft.Row(
                [message_input, ft.IconButton(icon="send", on_click=send_message)],
                spacing=10
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        scroll=ft.ScrollMode.ALWAYS
    )

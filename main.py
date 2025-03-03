import flet as ft

def generate(prompt):
    # Add your AI generation logic here
    print(f"Generating app for prompt: {prompt}")

def main(page: ft.Page):
    # Page settings
    page.title = "AppGen AI"
    page.bgcolor = "#000000"
    page.scroll = "adaptive"
    page.padding = 40

    # UI Elements
    header = ft.Column(
        controls=[
            ft.Text(
                "AppGen AI",
                size=48,
                weight="bold",
                text_align="center",
                color="#ffffff"
            ),
            ft.Text(
                "Turn text prompts into cross-platform apps instantly",
                size=24,
                text_align="center",
                color="#ffffff"
            )
        ],
        spacing=20,
        horizontal_alignment="center"
    )

    prompt_field = ft.TextField(
        multiline=True,
        min_lines=5,
        max_lines=5,
        border_color="#ffffff",
        color="#ffffff",
        cursor_color="#ffffff",
        text_align="center",
        hint_text="Describe your app...",
        hint_style=ft.TextStyle(color="#888888"),
        on_submit=lambda e: generate(e.control.value)
    )

    generate_button = ft.ElevatedButton(
        text="Generate App",
        icon=ft.icons.AUTO_GRAPH,
        on_click=lambda e: generate(prompt_field.value),
        color="#000000",
        bgcolor="#ffffff"
    )

    # Layout
    page.add(
        ft.Column(
            [
                header,
                ft.Divider(height=40, color="transparent"),
                ft.Container(
                    prompt_field,
                    alignment=ft.alignment.center,
                    width=800
                ),
                ft.Divider(height=20, color="transparent"),
                ft.Container(
                    generate_button,
                    alignment=ft.alignment.center
                )
            ],
            spacing=0,
            expand=True,
            horizontal_alignment="center",
            alignment="center"
        )
    )

ft.app(target=main)
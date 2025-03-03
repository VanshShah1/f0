import flet as ft

def main(page: ft.Page):
    page.title = "Scrollable App Layout"
    page.window_width = 800
    page.window_height = 600

    # Create scrollable column on the left
    left_column = ft.ListView(
        width=200,
        spacing=10,
        padding=20,
        controls=[
            ft.ElevatedButton(f"Item {i}") 
            for i in range(30)  # Creates 30 buttons to demonstrate scrolling
        ]
    )

    # Create text editor on the right
    text_editor = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=30,
        value="Start typing...",
        border=ft.InputBorder.NONE,
        content_padding=20
    )

    # Create main layout
    main_layout = ft.Row(
        controls=[
            left_column,
            ft.VerticalDivider(width=1),
            text_editor,
        ],
        expand=True
    )

    page.add(main_layout)

ft.app(target=main)
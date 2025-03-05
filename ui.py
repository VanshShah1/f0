import flet as ft

def main(page: ft.Page):
    page.title = "TikTok-like Media Scroll"
    page.bgcolor = ft.colors.WHITE
    page.padding = (0, 20, 0, 20)
    page.scroll = ft.ScrollMode.ALWAYS
    
    def create_media_component():
        return ft.Container(
            gradient=ft.LinearGradient(["#1e3c72", "#2a5298"]),
            border_radius=15,
            padding=20,
            expand=True,
            content=ft.Column([
                ft.Container(
                    expand=True,
                    content=ft.Image(
                        src=f"image.jpg",
                        fit=ft.ImageFit.COVER,
                        border_radius=10,
                        scale=1
                    ),
                ),
                ft.Column(
                    spacing=20,
                    controls=[
                        ft.ElevatedButton(
                            text="Share",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                        ),
                        ft.ElevatedButton(
                            text="Comment",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                        )
                    ]
                )
            ])
        )

    page.add(
        ft.ResponsiveRow(
            [create_media_component()],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
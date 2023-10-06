import flet as ft

def main(page: ft.Page):
    btn = ft.ElevatedButton('Clica-me!')

    page.add(btn)

ft.app(target=main)

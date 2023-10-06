import flet as ft

def main(page: ft.Page):
    t=ft.Text(value='Olá Mundo', color='red')
    page.controls.append(t)
    page.update()

ft.app(target=main)

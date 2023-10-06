import flet as ft

def main(page: ft.Page):
    lbl_texto=ft.Text(value='Olá Mundo', color='red')
    page.controls.append(lbl_texto)
    page.update()

ft.app(target=main)

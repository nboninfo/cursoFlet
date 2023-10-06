import flet as ft

def main(page: ft.Page):

    txt_nome=ft.TextField(label='Digite seu nome')
    lbl_ola = ft.Text()

    def click(e):
        lbl_ola.value=f'Olá... {txt_nome.value}!'
        page.update()

    row = ft.Row(controls=[
        txt_nome,
        ft.ElevatedButton(text='Clicke-me', on_click=click),
        lbl_ola
    ])
    page.add(row)

ft.app(target=main, view=ft.WEB_BROWSER)
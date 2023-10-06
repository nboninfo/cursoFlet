import flet as ft

def main(page: ft.Page):

    txt_nome=ft.TextField(label='Digite seu nome')

    def click(e):
        print(f'Olá...{txt_nome.value}!')

    row = ft.Row(controls=[
        txt_nome,
        ft.ElevatedButton(text='Clicke-me', on_click=click)
    ])
    page.add(row)

ft.app(target=main)
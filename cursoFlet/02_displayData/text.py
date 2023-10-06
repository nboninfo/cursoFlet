import flet as ft

def main(page: ft.Page):
    txt_texto = ft.Text(
        value= 'Este é um exemplo de controlo de texto',
        size=30,
        color='white',
        bgcolor='red',
        weight='bold',
        italic=True
    )
    
    page.add(txt_texto)

ft.app(target=main)
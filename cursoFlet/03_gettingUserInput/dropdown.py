import flet
from flet import Dropdown, ElevatedButton, Page, Text, dropdown

def main(page):
    def btn_click(e):
        saida_txt.value = f'O Valor do Dropdown es: {cor_drop.value}'
        page.update()

    saida_txt = Text()
    enviar_btn = ElevatedButton(text='enviar', on_click=btn_click)
    cor_drop = Dropdown(
        width=100,
        options=[
            dropdown.Option('Vermelho'),
            dropdown.Option('Verde'),
            dropdown.Option('Azul'),
        ],
    )
    
    page.add(cor_drop, enviar_btn, saida_txt)

flet.app(target=main)

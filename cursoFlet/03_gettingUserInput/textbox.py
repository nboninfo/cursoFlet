import flet
from flet import ElevatedButton, Text, TextField

def main(page: flet.Page):
  
    def ola_click(e):
        if not txt_nome.value:
            txt_nome.error_text='Por favor introduz teu nome'
            page.update()
        else:
            name = txt_nome.value
            page.clean()
            page.add(Text(f'Olá {name}!'))

    txt_nome = TextField(label='Qual é seu nome?')
    btn_click = ElevatedButton('Olá!', on_click=ola_click)

    page.add(
        txt_nome,
        btn_click
    )

flet.app(target=main)

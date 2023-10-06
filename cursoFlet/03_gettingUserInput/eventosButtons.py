import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title = 'Exemplo dum contador em FLET'
    page.vertical_alignment = 'center'

    txt_numero = TextField(value='0', text_align='center', width=100)

    def reducir_click(e):
        txt_numero.value = int(txt_numero.value) -1
        page.update()
    def aumentar_click(e):
        txt_numero.value = int(txt_numero.value) +1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=reducir_click),
                txt_numero,
                IconButton(icons.ADD, on_click=aumentar_click),
            ],
            alignment='center',
        )
    )

flet.app(target=main)

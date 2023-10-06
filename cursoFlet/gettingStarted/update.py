import time
import flet as ft

def main(page: ft.Page):
    lbl_texto = ft.Text()
    page.add(lbl_texto)

    for i in range(10):
        lbl_texto.value=f'Step: {i}'
        page.update()

        time.sleep(1)

ft.app(target=main)

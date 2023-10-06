import flet as ft

def main(page: ft.Page):
    txt_primeiro_nome=ft.TextField(label='Primeiro Nome', autofocus=True)
    txt_ultimo_nome=ft.TextField(label='Segundo Nome')
    txt_ola=ft.Column()

    def btn_clicked(e):
        txt_ola.controls.append(ft.Text(f'Ola, {txt_primeiro_nome.value} {txt_ultimo_nome.value}!'))
        txt_primeiro_nome.value=''
        txt_ultimo_nome.value=''
        page.update()
        txt_primeiro_nome.focus()

    btn_clicked=ft.ElevatedButton(text='Diga Olá', on_click=btn_clicked)

    page.add(
        txt_primeiro_nome,
        txt_ultimo_nome,
        btn_clicked,
        txt_ola,        
    )  

ft.app(target=main)
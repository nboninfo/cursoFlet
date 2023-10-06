import flet as ft

def main(page: ft.Page):
    txt_primeiro_nome=ft.TextField(label='Primeiro Nome')
    txt_ultimo_nome= ft.TextField(label='Segundo Nome')
    
    #desabilitando os campos individualmente
    txt_ultimo_nome.disabled=True

    page.add(txt_primeiro_nome, txt_ultimo_nome)

    #desabilitando os dois ao mesmo tempo
    coluna = ft.Column(controls=[
        txt_primeiro_nome,
        txt_ultimo_nome
    ])
    
    coluna.disabled=True
    
    page.add(coluna)

ft.app(target=main)
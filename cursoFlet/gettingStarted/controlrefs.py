import flet as ft

def main(page: ft.Page):
    txt_primeiro_nome=ft.TextField(label='Primeiro Nome', autofocus=True)
    txt_ultimo_nome=ft.TextField(label='Segundo Nome')
    txt_ola=ft.Column()
    
    def btn_clicked(e):
        if txt_primeiro_nome.value=='':
            txt_ola.controls.append(ft.Text('Todos os campos devem ser preenchidos'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
            txt_primeiro_nome.value=''
            txt_ultimo_nome.value=''
            page.update()
            txt_primeiro_nome.focus()
        elif txt_ultimo_nome.value=='':
            txt_ola.controls.append(ft.Text('Todos os campos devem ser preenchidos'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
            txt_primeiro_nome.value=''
            txt_ultimo_nome.value=''
            page.update()
            txt_primeiro_nome.focus()
        else:
            txt_ola.controls.append(ft.Text(f'Ola, {txt_primeiro_nome.value} {txt_ultimo_nome.value}!'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
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
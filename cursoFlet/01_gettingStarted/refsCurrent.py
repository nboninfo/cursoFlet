import flet
from flet import Column, ElevatedButton, Text, TextField, Ref

def main(page: flet.Page):
    txt_primeiro_nome=Ref[TextField]()
    txt_ultimo_nome=Ref[TextField]()
    col_ola=Ref[Column]()
    
    def btn_clicked(e):
        if txt_primeiro_nome.current.value=='':
            col_ola.current.controls.append(Text('Todos os campos devem ser preenchidos'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
            txt_primeiro_nome.current.value=''
            txt_ultimo_nome.current.value=''
            page.update()
            txt_primeiro_nome.current.focus()
        elif txt_ultimo_nome.current.value=='':
            col_ola.current.controls.append(Text('Todos os campos devem ser preenchidos'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
            txt_primeiro_nome.current.value=''
            txt_ultimo_nome.current.value=''
            page.update()
            txt_primeiro_nome.current.focus()
        else:
            col_ola.current.controls.append(Text(f'Ola, {txt_primeiro_nome.current.value} {txt_ultimo_nome.current.value}!'))
            #limpa os campos depois de dar o erro ou estar certo atualiza o app e coloca o cursor no campo txt_priomeiro_nome
            txt_primeiro_nome.current.value=''
            txt_ultimo_nome.current.value=''
            page.update()
            txt_primeiro_nome.current.focus()

    btn_clicked=ElevatedButton(text='Diga Olá', on_click=btn_clicked)

    page.add(
        TextField(ref=txt_primeiro_nome, label='Primeiro Nome', autofocus=True),
        TextField(ref=txt_ultimo_nome, label='Ultimo Nome'),
        btn_clicked,
        Column(ref=col_ola)        
    )  

flet.app(target=main)
import flet
from flet import Checkbox, ElevatedButton, Row, TextField

def main(page: flet.Page):
    
    def add_tarefa(e):
        page.add(Checkbox(label=nova_tarefa.value))

    nova_tarefa=TextField(hint_text='Que tarefa quer adicionar?', width=300)
    btn_adicionar=ElevatedButton('Adicionar', on_click=add_tarefa)
    
    page.add(Row([nova_tarefa, btn_adicionar]))

flet.app(target=main)
import flet
from flet import Checkbox, Text

def main(page: flet.Page):
    def checkbox_chaged(e):
        output_txt.value = (f'Você aprendeu a programar : {todo_check.value}.')
        page.update()
    
    output_txt = Text()
    todo_check = Checkbox(label='ToDo: Aprender a programar', value=False, on_change=checkbox_chaged)
    
    page.add(todo_check, output_txt)

flet.app(main)
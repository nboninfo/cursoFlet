import flet as ft

def main(page: ft.Page):
    #forma original da documentação
    page.add(
    ft.Row(controls=[
        ft.Text('Flet'),
        ft.Text('Python'),
        ft.Text('Flutter')
    ])
)
    
    #minha forma simples
    row_dados = ft.Row(controls=[ft.Text('Flet'), ft.Text('Flutter'), ft.Text('Python')])
    page.add(row_dados)

    #outra forma
    lenguagem = ['Python', 'Flutter', 'Flet']
    labels = []

    for e in lenguagem:
        labels.append(ft.Text(e))
    row_dados_um = ft.Row(controls=labels)

    page.add(row_dados_um)


ft.app(target=main)
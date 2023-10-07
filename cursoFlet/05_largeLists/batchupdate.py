import flet as ft

def main(page: ft.Page):

    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(ft.Text(f"Line {i}"))
        if i % 100 == 0:
            page.update()
    page.update()

ft.app(target=main)
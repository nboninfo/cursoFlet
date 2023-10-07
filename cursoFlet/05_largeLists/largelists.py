import flet
from flet import Page, Text

def main(page: Page):
    for i in range(5000):
        page.controls.append(Text(f'Linha {i}'))
    page.scroll = 'always'
    page.update()

flet.app(target=main)
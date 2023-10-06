import flet
from flet import KeyboardEvent, Page, Text

def main(page):
    def on_keyboard(e: KeyboardEvent):
        page.add(Text(f'Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}'))

    page.on_keyboard_event = on_keyboard
    page.add(Text('Pressione qualquer tecla com uma combinação de teclas CTRL, ALT, SHIFT e META...'))

flet.app(target=main)

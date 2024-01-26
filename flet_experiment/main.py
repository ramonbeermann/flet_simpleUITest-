# Look: https://flet.dev

import flet  as ft
from flet import IconButton,Page,Row, TextField, icons

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"


    txt_number = TextField(value="0", text_align="center", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1 
        page.update()


    page.add(
        Row(
        [
            IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_number, 
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,

        )
    )    
ft.app(target=main)

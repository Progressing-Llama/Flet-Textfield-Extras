import threading
import time

import flet as ft

from flet_textfield_extras import FletTextfieldExtras
from flet_textfield_extras.flet_textfield_extras import TextSelection


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def update(e: TextSelection):
        pass

    tf = FletTextfieldExtras(
        tooltip="My new FletTextfieldExtras Control tooltip",
        value = "My new FletTextfieldExtras Flet Control",
        multiline=True,
        on_selection_change=update,
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.PINK)

    page.add(
        ft.Container(height=150, width=300, alignment = ft.alignment.center, content=tf,),
    )
    tf.focus()

    def sleep():
        for i in range(0, 10):
            time.sleep(3)
            tf.set_selection(5, 10 + i)
            print(i)

    threading.Thread(target=sleep).start()


ft.app(main)

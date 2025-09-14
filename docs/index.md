# Introduction

FletTextfieldExtras for Flet.

## Examples

```
import flet as ft

from flet_textfield_extras import FletTextfieldExtras


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletTextfieldExtras(
                    tooltip="My new FletTextfieldExtras Control tooltip",
                    value = "My new FletTextfieldExtras Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletTextfieldExtras](FletTextfieldExtras.md)



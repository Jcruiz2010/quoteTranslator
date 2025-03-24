import flet as ft

def main(page: ft.Page):
    
    quote = ft.Text("The rest is silence.")
    radio_group = ft.RadioGroup(
        content= ft.Column(
            controls=[
                ft.Radio(label="Spanish", value= "El resto es silencio."),
                ft.Radio(label="Hebrew", value= "השאר זה שקט"),
                ft.Radio(label="French", value= "Le reste est silence.")
            ]
        )
    )

ft.app(target=main,assets_dir="assets")
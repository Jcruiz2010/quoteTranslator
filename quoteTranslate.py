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

    def translation(e):
        if radio_group.value == "El resto es silencio.":
            quote.value = radio_group.value
        elif radio_group.value == "השאר זה שקט":
            quote.value = radio_group.value
        else:
            quote.value = radio_group.value
        page.update()
 
    translation_button = ft.ElevatedButton("Submit", on_click=translation)
    hamletImage = ft.Image(src="hamlet.jpeg", visible=True, height= 240, width=240)
    page.add(quote,radio_group,translation_button, hamletImage)

ft.app(target=main,assets_dir="assets")
import flet as ft
import qr
import base64
import os
from io import BytesIO
from PIL import Image

def main(page: ft.Page):
    page.title = "De MijnGang - QR Code Creator & Scanner"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Functions
    ## Generate a QR code
    def create_qr(e):
        # Disable buttons to prevent spamming
        button_create.disabled = True
        button_save.disabled = True
        button_create.update()
        button_save.update()

        # Replace image
        image_qr.src = ""
        image_qr.src_base64 = qr.create_code(value_name.value, value_birthday.value)

        # Re-enable buttons
        button_create.disabled = False
        button_save.disabled = False

        # Update text
        txt_status.value = f"Code met waarde {value_name.value}|{value_birthday.value} gegenereerd!"

        create.update()

    ## Save generated QR code
    def save_qr(e):
        to_save = base64.b64decode(image_qr.src_base64)
        image = Image.open(BytesIO(to_save))
        image.save(f"saved/{value_name.value}.png")

        # Show where image is saved
        txt_status.value = f"Afbeelding opgeslagen naar 'saved/{value_name.value}.png'!"

        create.update()

    ## Open saved image directory
    def open_folder(e):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(path, "saved")
        os.startfile(path)

    # 'Create' tab
    value_name = ft.TextField(label="Naam")
    value_birthday = ft.TextField(label="Geboortedatum")
    button_create = ft.FilledButton(text = "Maak", on_click = create_qr)
    button_save = ft.FilledButton(text = "Opslaan", disabled = True, on_click = save_qr)
    button_folder = ft.IconButton(icon = ft.Icons.FOLDER_OPEN, icon_size = 20, tooltip = "Open folder", on_click = open_folder)
    image_qr = ft.Image(height = 300, width = 300, src = "images/Placeholder.png")
    txt_status = ft.Text("Status tekst.")

    create = ft.Column([
        ft.Container(content = ft.Text("Maak een QR code", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM), alignment = ft.alignment.top_center),
        ft.Row([ft.Container(content=value_name), ft.Container(content=value_birthday)], spacing = 30, alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([button_create, button_save], spacing = 30, alignment = ft.MainAxisAlignment.CENTER),
        ft.Container(content = image_qr, alignment = ft.alignment.center),
        ft.Row([ft.Container(content = txt_status, alignment = ft.alignment.bottom_center), button_folder], spacing = 30, alignment = ft.MainAxisAlignment.CENTER)   
        ],
        spacing = 25
    )

    # 'Scan' tab
    scan = ft.Column([
        ft.Container(content = ft.Text("Scan een QR code", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM), alignment = ft.alignment.top_center)
    ],
    spacing = 25
    )

    # Finalize
    create_tab = ft.Tab(text="Maak", content=create)
    scan_tab = ft.Tab(text="Scan", content=scan)
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[create_tab, scan_tab],
        expand=1
    )
    page.add(t)
    
# Run 
ft.app(main, assets_dir="assets")
import flet as ft
import base64, os, sys, keyboard, re
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from io import BytesIO
from PIL import Image

def main(page: ft.Page):
    page.title = "De MijnGang - QR Code Creator & Scanner"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create QR code
    ## Functions
    def generate_code(e):
        # Disable buttons to prevent spamming
        button_create.disabled = True
        button_save.disabled = True
        button_create.update()
        button_save.update()

        # Loading icon

        # Generate QR code
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        # qr.add_data(f"{textfield_name.value}|{textfield_birthday.value}")
        qr.add_data(f"Naam: {textfield_name.value}, Geboortedatum: {textfield_birthday.value}")
        image = qr.make_image()
        
        # Convert to base64 string
        bio = BytesIO()
        image.save(bio, 'PNG')
        b64 = base64.b64encode(bio.getvalue()).decode("utf-8")
        
        # Replace image
        image_qr.src = ""
        image_qr.src_base64 = b64

        # Re-enable buttons
        button_create.disabled = False
        button_save.disabled = False

        # Update status text
        text_status.value = f"Code met waarde {textfield_name.value} | {textfield_birthday.value} gegenereerd!"

        # Update page
        create_col.update()

    def save_code(e):
        # Convert base64 to image
        code = base64.b64decode(image_qr.src_base64)

        # Save QR code
        image = Image.open(BytesIO(code))
        image.save(f"saved/{textfield_name.value}.png")

        # Update status text
        text_status.value = f"Afbeelding opgeslagen naar 'saved/{textfield_name.value}.png'!"

        # Update page
        create_col.update()

    def open_directory(e):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(path, "saved")
        os.startfile(path)

    ## Dynamic variables
    textfield_name = ft.TextField(label="Naam")
    textfield_birthday =  ft.TextField(label="Geboortedatum")
    button_create = ft.FilledButton(text = "Maak", on_click = generate_code)
    button_save = ft.FilledButton(text = "Opslaan", disabled = True, on_click = save_code)
    button_folder = ft.IconButton(icon = ft.Icons.FOLDER_OPEN, icon_size = 20, tooltip = "Open folder", on_click = open_directory)
    image_qr = ft.Image(height = 300, width = 300, src = "images/Placeholder.png")
    text_status = ft.Text("Status tekst.")

    ## Column view
    create_col = ft.Column([
        ft.Container(content = ft.Text("Maak een QR code", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM), alignment = ft.alignment.top_center),
        ft.Row([ft.Container(content=textfield_name), ft.Container(content=textfield_birthday)], spacing = 30, alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([button_create, button_save], spacing = 30, alignment = ft.MainAxisAlignment.CENTER),
        ft.Container(content = image_qr, alignment = ft.alignment.center),
        ft.Row([ft.Container(content = text_status, alignment = ft.alignment.bottom_center), button_folder], spacing = 30, alignment = ft.MainAxisAlignment.CENTER)   
        ],
        spacing = 25
    )

    # Scan QR code
    ## Functions
    def toggle_scan(e):
        # Flip boolean ~ TODO
        global is_scanning
        is_scanning = not is_scanning
        print(is_scanning)

        # Change button color depending on state
        if (is_scanning):
            button_record.icon_color=ft.Colors.RED_900
        else:
            button_record.icon_color=ft.Colors.RED_100

        # Update button
        button_record.update()

    def scan_code():
        # Scan keyboard input (ideally only from scanner)
        qr_data = ""

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "enter":
                    break
                else:
                    qr_data += event.name
    
        # Clean data with regex
        cleaned_data = re.sub(r"(shift|delete)", "", qr_data)
        cleaned_data = re.sub(r"(space)", " ", cleaned_data)
        
        #dummy data: "Justin Muris|18-08-1999"
        
        return cleaned_data

    ## Dynamic variables
    is_scanning = False
    text_name = ft.Text("Naam: ")
    text_birthday = ft.Text("Verjaardag: ")
    button_record = ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED, icon_color=ft.Colors.RED_100, icon_size=20, tooltip="Scan", on_click=toggle_scan)

    ## Column view
    scan_col = ft.Column([
        ft.Container(content = ft.Text("Scan een QR code", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM), alignment = ft.alignment.top_center),
        ft.Row([ft.Container(content=text_name), ft.Container(content=text_birthday)], spacing = 30, alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([button_record], spacing = 30, alignment = ft.MainAxisAlignment.CENTER)
        ],
        spacing = 25
    )

    # Finalize
    create_tab = ft.Tab(text="Maak", content=create_col)
    scan_tab = ft.Tab(text="Scan", content=scan_col)
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[create_tab, scan_tab],
        expand=1
    )
    page.add(t)
    
# Run 
ft.app(main, assets_dir="assets")
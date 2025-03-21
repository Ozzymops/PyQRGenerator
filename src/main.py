import flet as ft

def main(page: ft.Page):
    page.title = "De MijnGang - QR Code Creator & Scanner"
    
    # Create a QR code
    create = ft.Stack([
        ft.Container(content=ft.Text("Maak een QR code"), alignment=ft.alignment.top),
        ft.Container(content=ft.TextField(label="Naam"), alignment=ft.alignment.top),
        ft.Container(content=ft.TextField(label="Geboortedatum"), alignment=ft.alignment.top),
        ],
        width=300,
        height=300
    )

    
    # Scan a QR code
   
    # Tabs
    create_tab = ft.Tab(text="Maak", content=create)
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[create_tab],
        expand=1
    )
    page.add(t)
    
    
ft.app(main)

import sys
import keyboard
import qrcode
import re
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def create_code():
    # Data
    name = "Justin Muris"
    bday = "18-08-1999"

    qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(f"{name}|{bday}")

    # Style
    image = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

    # Export
    image.save(name + ".png")

create_code()

def capture_qr_data():
    qr_data = ""
    print("Scan a QR code...")

    # Continuously capture the keys pressed
    while True:
        event = keyboard.read_event()  # Read the next event
        if event.event_type == keyboard.KEY_DOWN:  # Only consider key press events
            if event.name == "enter":  # If Enter key is pressed, stop capturing
                break
            else:
                qr_data += event.name  # Append the key pressed to qr_data
    
    # Clean
    cleaned_data = re.sub(r"(shift|delete)", "", qr_data)
    cleaned_data = re.sub(r"(space)", " ", cleaned_data)
    
    #dummy data: "Justin Muris|18-08-1999"
    
    return cleaned_data

# Main function to handle QR code scan
if __name__ == "__main__":
    qr_code = capture_qr_data()  # Capture the QR code data
    print(f"QR Code Scanned: {qr_code}")
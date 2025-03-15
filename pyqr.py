import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Data
name = sys.argv[1]
bday = sys.argv[2]
teln = sys.argv[3]

qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
qr.add_data("Naam: {fname}\nGeboortedatum: {fbday}\nTelefoonnummer: {fteln}".format(fname = name, fbday = bday, fteln = teln))

# Style
image = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

# Export
image.save(name + ".png")
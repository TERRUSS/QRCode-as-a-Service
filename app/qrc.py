from enum import Enum
import qrcode, io, base64
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, CircleModuleDrawer

class qrc:
    qr = qrcode.QRCode(box_size=20)
    class img(Enum):
        classic = SquareModuleDrawer
        vertical_bars = VerticalBarsDrawer
        horisontal_bars = HorizontalBarsDrawer
        rounded = RoundedModuleDrawer
        dots = CircleModuleDrawer


    def __init__(self, inp):
        self.qr.clear()
        self.qr.add_data(inp)

    def print_ascii(self):
        f = io.StringIO()
        self.qr.print_ascii(out=f)
        f.seek(0)
        return f.read()

    def gen_img(self, drawer=None):
        if drawer:
            img = self.qr.make_image(image_factory=StyledPilImage, module_drawer=drawer.value())
        else:
            img = self.qr.make_image()

        buff = io.BytesIO()
        img.save(buff, format='png')
        return "data:image/jpeg;base64," + base64.b64encode(buff.getvalue()).decode('utf-8')
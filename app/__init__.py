from flask import Flask, request
from flask_accept import accept, accept_fallback

from enum import Enum
import qrcode, io, base64
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, CircleModuleDrawer

class qrc:
    qr = qrcode.QRCode()
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
        print(self.img.__members__)
        if drawer:
            img = self.qr.make_image(image_factory=StyledPilImage, module_drawer=drawer.value())
        else:
            img = self.qr.make_image()

        buff = io.BytesIO()
        img.save(buff, format='png')
        return "data:image/jpeg;base64," + base64.b64encode(buff.getvalue()).decode('utf-8')



def create_app():
    app = Flask(__name__)

    @app.route('/<path:inp>', methods=['GET', 'POST'])
    @accept_fallback
    def home(inp):
        qr = qrc(inp)
        return f'Here is your qrcode for {inp} : {qr.print_ascii()}'
    
    @home.support('text/html')
    def home_html(inp):
        qr = qrc(inp)
        return f'<h1>qrcode as a service</h1>Here is your qrcode for {inp} : <pre>{qr.print_ascii()}</pre><img src={qr.gen_img(qr.img.vertical_bars)} />'


    @home.support('image/png')
    def home_img(inp):
        qr = qrc(inp)

        if request.method == 'POST':
            print(request)
            return qr.gen_img( qr.img[request.json['drawer']] if request.json['drawer'] in qr.img.__members__ else False )

        return qr.gen_img(qr.img.classic)
    return app

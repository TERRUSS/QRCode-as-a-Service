
import app

def run():
    qr = app.qrc('test')
    print(qr.print_ascii())

    print(qr.gen_img())

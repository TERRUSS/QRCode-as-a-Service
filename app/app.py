#!/usr/bin/env python3

import sys
sys.path.append('/root/QRCode-as-a-Service/env/lib/python3.9/site-packages/pip')

from flask import Flask, request, send_from_directory
from flask_accept import accept, accept_fallback

from qrc import qrc

import os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "front", "dist")
print(root)

def create_app():
    app = Flask(__name__)

    @app.route('/<path:inp>', methods=['GET', 'POST'])
    @accept_fallback
    def home(inp):
        print(inp, request.headers)
        if inp == "assets/vendor.js":
            return send_from_directory(root, 'assets/vendor.js', mimetype='text/javascript')
        qr = qrc(inp)
        return f'Here is your qrcode for `{inp}` : { qr.print_ascii() }'
    
    @home.support('text/html')
    def home_html(inp):
        print("AAAA", inp)
        if inp == "assets/vendor.js":
            return send_from_directory(root, 'assets/vendor.js', mimetype='text/javascript')
        return send_from_directory(root, 'index.html')


    # @home.support('text/css')
    # def home_html(path):
    #     return send_from_directory(root, path)

    @home.support('image/png')
    def home_img(inp):
        qr = qrc(inp)

        if request.method == 'POST':
            return qr.gen_img( qr.img[request.json['drawer']] if 'drawer' in request.json.keys() and request.json['drawer'] in qr.img.__members__ else False )

        return qr.gen_img(qr.img.classic)

    @app.route('/*')
    def a():
        return redirect('awesome%20qrcode')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

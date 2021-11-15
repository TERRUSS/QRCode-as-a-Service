#!/usr/bin/env python3

import sys
import os
sys.path.append('/root/QRCode-as-a-Service/env/lib/python3.9/site-packages/pip')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(os.listdir(SCRIPT_DIR))
print(sys.version)

from app import create_app
application = create_app()

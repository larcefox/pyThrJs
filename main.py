#!/home/larce/projects/conote/env/bin/python
# -*- coding: utf-8 -*-
"""pythr.py: Visual modeling helper."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import socketserver
from lib.server_start import HTTP_SERVER

def run(hendler_class=HTTP_SERVER, port=9000):
    server_address = ('0.0.0.0', port)
    httpd = socketserver.TCPServer(server_address, hendler_class)
    print('server started')
    httpd.serve_forever()

run()

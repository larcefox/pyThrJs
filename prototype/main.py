# -*- coding: utf-8 -*-

from http import server
from js_template import TemplateRender
import socketserver 
from pathlib import Path
from tree_test import main as data


class MyHandler(server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js':'application/x-javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
        }
    def _set_headers(self):

        self.send_response(200)
        if self.path == '/':
            self.send_header(
                    'Content-type', 
                    'text/html'
                    )
        elif self.path == '/data':
            self.send_header(
                    'Access-Control-Allow-Origin',
                    '*'
                    # 'Content-type', 'application/json'
                    )
        else:
            self.send_header(
                    'Content-type', 
                    self.guess_type(self.path)
                    )

        self.end_headers()

    def do_GET(self): # handle GET request

        templates_path = Path(__file__).parent.absolute().joinpath('templates')
        src_path = templates_path.joinpath(self.path[1:]) # skip first simbol, because joinpath not work with it
        template = TemplateRender()
        self._set_headers()

        if self.path == '/':
            self.wfile.write(template('index.html', 'title', 'body'))

        # if it executes python script with JQuery
        elif '?_=' in self.path:
            current_path = src_path.parent / src_path.name.split('?_=')[0]
            with open(current_path, 'rb') as f:
                self.wfile.write(f.read())
            print(current_path)

        elif src_path.exists():
            print(src_path.exists())
            with open(src_path, 'rb') as f:
                self.wfile.write(f.read())

        elif self.path == '/data':
            self.wfile.write(bytes(data(), 'utf-8'))

        elif not src_path.exists():
            self.wfile.write(template('404.html', 'title', 'body'))


        print(self.path)

def run(handler_class=MyHandler, port=9000):
    server_address = ('0.0.0.0', port)
    httpd = socketserver.TCPServer(server_address, handler_class)
    print("Starting server...")
    httpd.serve_forever()
run()

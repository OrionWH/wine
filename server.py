#!/usr/bin/env python3
"""
     ---=== RUBOT ===---
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from http import cookies
import logging
import os
import threading
import urllib.parse
from urllib.parse import parse_qs
import json
import requests
import ast
import time
from parser import Parser

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Set-Cookie', 'UID=blblblblblb')
        self.send_header('Set-Cookie', 'UIDa=2222')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        p = Parser()
        if str(self.path) == "/":
            page_path = "_public/index.tt"
        else:
            page_path = "_public/{}.tt".format(str(self.path))
        self.wfile.write(p.read_page(page_path).encode('utf-8'))
        

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("OK from POST")
        
        
def run(server_class=ThreadingHTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

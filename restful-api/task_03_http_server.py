#!/usr/bin/python3
"""
Module to set up a basic HTTP server
"""
import http.server
import json
from http import HTTPStatus


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API")
        elif self.path == '/data':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port 8000...")
    httpd.serve_forever()

if __name__ =="__main__":
    run()

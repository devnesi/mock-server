#!/usr/bin/env python3
import http.server as SimpleHTTPServer
import socketserver as SocketServer
import json
PORT = 8000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({'status':'OK'}).encode(encoding='utf_8'))

httpd = SocketServer.TCPServer(("0.0.0.0", PORT), GetHandler)
httpd.serve_forever()

#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs, unquote, quote
import sys, subprocess
from ss_tagger import tagger

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        global t
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        rl = self.requestline
        query = rl.split(' ')[1][2:]
        data = parse_qs(query)['data'][0].strip('\"')
        json_tagged_data = t.json(data)
        self.wfile.write(json_tagged_data.encode())
        return

try:
    global t
    print("Initializing tagger. (~45 seconds)")
    t = tagger()
    print("Tagger initialized. Starting server.")
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' + str(PORT_NUMBER)+ ".")
    print("CTRL-C to kill server.")
        
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()

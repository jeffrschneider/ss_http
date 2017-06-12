#!/usr/bin/env python3
#encoding: utf-8
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs, unquote, quote
import sys, subprocess, unicodedata, re
from ss_tagger import tagger

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        unicode_whitespaces = []
        
        global t
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        rl = self.requestline
        query = rl.split(' ')[1][2:]
        query = unquote(query)
        query = re.sub('\s', ' ', query) #replaces all unicode spaces with single ascii space
        query = unicodedata.normalize('NFKC', query) #converts unicode full width to half width ascii, along with some accent conversions
        data = parse_qs(query)['data'][0].strip('"').strip("'")
        print("data sent to tagger: " + data)
        json_tagged_data = t.json(data)
        self.wfile.write(json_tagged_data.encode("utf-8"))
        return

try:
    global t
    print("Initializing tagger. (~60 seconds)")
    t = tagger()
    print("Tagger initialized. Starting server.")
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' + str(PORT_NUMBER)+ '.')
    print("CTRL-C to kill server.")
        
    server.serve_forever()

except KeyboardInterrupt:
    print(' received, shutting down the web server')
    server.socket.close()

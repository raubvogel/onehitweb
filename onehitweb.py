#! /usr/bin/env python
'''
Simple dumb webserver to serve a file.
It will try to serve a file called preseed.cfg, located in the directory
program was called, on localhost:8000

The idea is you can ask for any file you want, and will get what we
give to you.

Based on https://wiki.python.org/moin/BaseHttpServer
http://www.acmesystems.it/python_httpserver
'''
import time
import BaseHTTPServer

HOST_NAME = '' # Accept requests on all interfaces
PORT_NUMBER = 8000
FILE = 'preseed.cfg'

def read_file(filename):
    '''
    Read in (text) file and return it as a string
    '''
    file = open(filename, "r")
    return file.read()

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        file = read_file(FILE)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(file)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

#! /usr/bin/env python
'''
Simple dumb webserver to serve a file. 
If no arguments are provided, it will try to serve a file called preseed.cfg,
located in the directory program was called, on localhost:8000

Based on https://wiki.python.org/moin/BaseWebServer
http://www.acmesystems.it/python_httpserver

Useful
http://stackoverflow.com/questions/18444395/basehttprequesthandler-with-custom-instance
http://www.mlsite.net/blog/?p=80

http://stackoverflow.com/questions/237432/python-properties-and-inheritance
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch08s08.html
http://www.opensource.apple.com/source/python/python-3/python/Lib/BaseHTTPServer.py
http://stackoverflow.com/questions/8333354/how-to-override-constructor-of-python-class-with-many-arguments

'''

import time
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import getopt
import sys

# Some default values in case they are not passed as arguments
HOST_NAME = '' 
PORT_NUMBER = 8000 
FILE = 'preseed.cfg'

class MyHandler(BaseHTTPRequestHandler):
    '''
    Extending __init__ so we can pass file
    '''
    def __init__(self, filename, *args):
        self.file = read_file(filename)
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(self.file)
	return

class WebServer:
    def __init__(self, filename, host, port):
        def handler(*args):
            MyHandler(filename, *args)
        self.server = HTTPServer((host, port), handler)

    def start(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass
        self.server.server_close()


def read_file(filename):
    '''
    Read in (text) file and return it as a string
    '''
    file = open(filename, "r")
    return file.read()

def print_usage():
    print "Usage:"
    print __file__ + " [filename] [host] [port]"

def main(filename = FILE, host = HOST_NAME, port = PORT_NUMBER):
    print "in main, file =", filename
    httpd = WebServer(filename, host, port)
    print time.asctime(), "Server Starts - %s:%s" % (host, port)
    httpd.start()
    print time.asctime(), "Server Stops - %s:%s" % (host, port)

if __name__ == '__main__':
   main(*sys.argv[1:])

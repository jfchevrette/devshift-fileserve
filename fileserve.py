#!/usr/bin/python2

import os
import sys

import SimpleHTTPServer
import SocketServer
import BaseHTTPServer

PORT = 8000
THEFILE = ''


class ServeFileHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        with open(THEFILE) as f:
            for line in f:
                s.wfile.write(line)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print "usage: %s <thefile>" % sys.argv[0]
        sys.exit(1)

    THEFILE = sys.argv[1]

    if not os.path.isfile(THEFILE):
        print "ERROR: file %s not found." % THEFILE
        sys.exit(1)

    SocketServer.TCPServer.allow_reuse_address = True
    httpd = SocketServer.TCPServer(("", PORT), ServeFileHandler)

    print "Serving file %s at port %s" % (THEFILE, PORT)
    httpd.serve_forever()

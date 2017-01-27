from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import datetime as dt
import json
from SocketServer import ThreadingMixIn
import sys


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        data = {'time': dt.datetime.now().isoformat()}
        body = json.dumps(data, indent=2)
        response = (
            "HTTP/1.0 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "Content-Length: %i\r\n\r\n%s" % (len(body), body))
        self.wfile.write(response)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def main(host, port):
    ThreadedHTTPServer((host, port), Handler).serve_forever()


if __name__ == '__main__':
    main('0.0.0.0', 8888)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import datetime as dt
import json
from SocketServer import ThreadingMixIn


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        data = {'datetime_iso': dt.datetime.now().isoformat()}
        self.wfile.write(json.dumps(data, indent=2))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


PORT = 8888


if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', PORT), Handler)
    server.serve_forever()

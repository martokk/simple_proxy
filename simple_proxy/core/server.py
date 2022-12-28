import socketserver
from http.server import SimpleHTTPRequestHandler
from urllib.request import urlopen

PORT = 7070


class MyProxy(SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        print(url)
        self.send_response(200)
        self.end_headers()
        source = urlopen(url=url)
        self.copyfile(source=source, outputfile=self.wfile)


def start_server():
    httpd = socketserver.ForkingTCPServer(("localhost", PORT), MyProxy)
    print("Listening...")
    httpd.serve_forever()

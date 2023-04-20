from http.server import HTTPServer, BaseHTTPRequestHandler


class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hola mundo!')


servidor = HTTPServer(('localhost', 80), MiServidor)
servidor.serve_forever()
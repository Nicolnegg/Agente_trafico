from http.server import HTTPServer, BaseHTTPRequestHandler


class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hola mundo!')


direccion_ip = '192.168.0.7' # especifica la dirección IP que deseas utilizar
puerto = 80 # especifica el puerto que deseas utilizar
servidor = HTTPServer((direccion_ip, puerto), MiServidor)
print(f'Servidor en {direccion_ip}:{puerto}')
servidor.serve_forever()
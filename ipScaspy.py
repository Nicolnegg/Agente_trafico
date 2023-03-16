from scapy.all import *
from scapy.layers.http import HTTPRequest

# Dirección IP del servidor web
dst_ip = "192.168.1.2"

# Puerto de destino para el servidor web
dst_port = 80

# Construir el paquete HTTP GET
http_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=dst_port)/HTTPRequest(Method='GET', Path='/')

# Enviar el paquete
http_request.show2()
sendp(http_request)
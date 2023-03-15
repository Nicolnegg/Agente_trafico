from scapy.layers.inet import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from scapy.all import *
from scapy.layers.http import HTTPRequest
import time
import random
import string

def send_http_request(dst_ip, dst_port, http_method, uri):
    # Crear una solicitud HTTP personalizada
    http_request = HTTPRequest(
        Method=http_method,
        Host="example.com",
        Path=uri,
        headers={"User-Agent": "Scapy/HTTP 1.1"}
    )
    # Crear un paquete TCP y adjuntar la solicitud HTTP personalizada
    tcp_packet = TCP(
        sport=RandShort(),
        dport=dst_port,
        flags="PA",
        seq=RandInt(),
        ack=RandInt(),
    ) / http_request
    # Enviar el paquete
    send(IP(dst=dst_ip) / tcp_packet)

# def generate_http_traffic():
#     # Crear una solicitud HTTP
#     http_request = scapy.all.Ether()/scapy.all.IP(dst="www.example.com")/scapy.all.TCP(dport=80)/scapy.all.Raw(load="GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
#     scapy.all.sendp(http_request)

# def generate_https_traffic():
#     # Crear una solicitud HTTPS
#     https_request = scapy.all.Ether()/scapy.all.IP(dst="www.example.com")/scapy.all.TCP(dport=443)/scapy.all.Raw(load="GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
#     scapy.all.sendp(https_request)

# def generate_ssh_traffic():
#     # Crear una solicitud SSH
#     ssh_request = scapy.all.Ether()/scapy.all.IP(dst="10.0.0.2")/scapy.all.TCP(dport=22, flags="S")
#     scapy.all.sendp(ssh_request)

# def generate_mail_traffic():
#     # Crear una solicitud de correo electrónico
#     mail_request = scapy.all.Ether()/scapy.all.IP(dst="mail.example.com")/scapy.all.TCP(dport=25)/scapy.all.Raw(load="HELO example.com\r\nMAIL FROM: user@example.com\r\nRCPT TO: user2@example.com\r\nDATA\r\nSubject: prueba de correo electrónico\r\nEste es un mensaje de prueba.\r\n.\r\nQUIT\r\n")
#     scapy.sendp(mail_request)

# def generate_ftp_traffic():
#     # Crear una solicitud FTP
#     ftp_request = scapy.all.Ether()/scapy.all.IP(dst="ftp.example.com")/scapy.all.TCP(dport=21)/scapy.all.Raw(load="USER anonymous\r\nPASS anonymous\r\nLIST\r\nQUIT\r\n")
#     scapy.sendp(ftp_request)

def generate_traffic():
    # Generar tráfico aleatorio
    while True:
        traffic_type = random.randint(1, 5)
        if traffic_type == 1:
            send_http_request("127.0.0.1", 80, "GET", "/index.html")
            print("HTTP")
        # elif traffic_type == 2:
        #     generate_https_traffic()
        #     print("HTTPS")
        # elif traffic_type == 3:
        #     generate_ssh_traffic()
        #     print("SSH")
        # # elif traffic_type == 4:
        #     generate_mail_traffic()
        # elif traffic_type == 5:
        #     generate_ftp_traffic()

        # Esperar un tiempo aleatorio antes de generar el siguiente tráfico

if __name__ == "__main__":
    traffic_interval = 5 # tiempo entre cada generación de tráfico, en segundos
    while True:
        generate_traffic()
        time.sleep(traffic_interval) 
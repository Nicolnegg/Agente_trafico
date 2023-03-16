from scapy.layers.inet import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from scapy.layers.tls.all import *
from scapy.layers.http import HTTPRequest
from faker import Faker
from scapy.all import *

import time
import random
import string


def generate_http_traffic():
    # Dirección IP del servidor web
    dst_ip = fake.ipv4_private()

    # Puerto de destino para el servidor web
    dst_port = 80

    # Construir el paquete HTTP GET
    http_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=dst_port)/HTTPRequest(Method='GET', Path='/')

    # Enviar el paquete
    http_request.show()
    sendp(http_request)

def generate_https_traffic():
    # Definimos los parámetros necesarios para la conexión
    dest_ip = fake.ipv4_private()
    dest_port = 443
    host = 'www.example.com'

     # Set up the three-way handshake
    syn = IP(dst=dest_ip) / TCP(dport=dest_port, flags='S')
    synack = sr1(syn)
    ack = IP(dst=dest_ip) / TCP(dport=dest_port, flags='A', ack=synack.seq + 1)

    # Generate the TLS handshake messages
    client_hello = TLS(
        record=TLS(
            handshake=TLS(
                client_hello=TLSClientHello(
                    version="TLS_1_2",
                    cipher_suites=[
                        0x9C,  # TLS_RSA_WITH_AES_128_CBC_SHA
                    ],
                    extensions=[
                        TLS_Ext_ServerName(servername=host),
                        TLS_Ext_SupportedGroups(groups=[23]),  # secp256r1
                        TLS_Ext_ECPointsFormat(ec_point_formats=[0]),  # uncompressed
                        TLS_Ext_SignatureAlgorithms(signature_algorithms=[0x0401])  # sha256 + rsa
                    ]
                )
            )
        )
    )

    # Send the TLS handshake messages
    client_hello.show()
    send(ack / client_hello)

    # Close the connection with a FIN
    fin = IP(dst=dest_ip) / TCP(dport=dest_port, flags='FA', seq=ack.ack, ack=synack.seq + 1)
    send(fin)

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
            print("HTTP")
            generate_http_traffic()            
        # elif traffic_type == 2:
        #     print("HTTPS")
        #     generate_https_traffic()
        #     
        # elif traffic_type == 3:
        #     generate_ssh_traffic()
        #     print("SSH")
        # # elif traffic_type == 4:
        #     generate_mail_traffic()
        # elif traffic_type == 5:
        #     generate_ftp_traffic()

        # Esperar un tiempo aleatorio antes de generar el siguiente tráfico

fake = Faker()
if __name__ == "__main__":
    traffic_interval = 10 # tiempo entre cada generación de tráfico, en segundos
    while True:
        
        
        generate_https_traffic()
        time.sleep(traffic_interval) 
        print("HTTPs")
        
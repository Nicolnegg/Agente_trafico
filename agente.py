from scapy.layers.http import HTTPRequest
from faker import Faker
from scapy.all import *

import requests
import time
import random


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

    fake = Faker()
    url = "https://" + fake.domain_name()
    response = requests.get('https://www.google.com', verify=True)
    print(response.content)
    
    
def generate_ssh_traffic():
    # Crear una solicitud SSH
    ssh_request = scapy.all.Ether()/scapy.all.IP(dst="10.0.0.2")/scapy.all.TCP(dport=22, flags="S")
    ssh_request.show()
    scapy.all.sendp(ssh_request)

def generate_mail_traffic():
    # Crear una solicitud de correo electrónico
    dst_ip = fake.ipv4_private()
    mail_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=25)/scapy.all.Raw(load="HELO example.com\r\nMAIL FROM: user@example.com\r\nRCPT TO: user2@example.com\r\nDATA\r\nSubject: prueba de correo electrónico\r\nEste es un mensaje de prueba.\r\n.\r\nQUIT\r\n")
    scapy.all.sendp(mail_request)

def generate_ftp_traffic():
    # Crear una solicitud FTP
    dst_ip = fake.ipv4_private()
    ftp_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=21)/scapy.all.Raw(load="USER anonymous\r\nPASS anonymous\r\nLIST\r\nQUIT\r\n")
    scapy.all.sendp(ftp_request)

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
        
from scapy.layers.http import HTTPRequest
from faker import Faker
from scapy.all import *

import requests
import time
import random
import paramiko


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

    #filtro http


def generate_https_traffic():

    url = fake.url()
    print(url)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTPS:", e)
    #filtro tls.handshake.type == 1 and tcp.port == 443 and ssl.handshake.extensions_server_name == "www.example.com"
    
def generate_ssh_traffic():
    # Crear una solicitud SSH
    # Crea una sesión SSH utilizando la biblioteca Paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('us01.vpnhack.xyz', username='vpnhack-root', password='123')
    # enviar comando a través de la conexión SSH
    stdin, stdout, stderr = ssh.exec_command('ls')
    # imprimir salida del comando
    print(stdout.read())
    # cerrar la conexión SSH
    ssh.close()
    #filtro ssh

def generate_mail_traffic():
    # Crear una solicitud de correo electrónico
    dst_ip = fake.ipv4_private()
    mail_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=25)/scapy.all.Raw(load="HELO example.com\r\nMAIL FROM: user@example.com\r\nRCPT TO: user2@example.com\r\nDATA\r\nSubject: prueba de correo electrónico\r\nEste es un mensaje de prueba.\r\n.\r\nQUIT\r\n")
    scapy.all.sendp(mail_request)
     #filtro smtp

def generate_ftp_traffic():
    # Crear una solicitud FTP
    dst_ip = fake.ipv4_private()
    ftp_request = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=21)/scapy.all.Raw(load="USER anonymous\r\nPASS anonymous\r\nLIST\r\nQUIT\r\n")
    scapy.all.sendp(ftp_request)
     #filtro ftp

def generate_traffic():
    # Generar tráfico aleatorio
    traffic_type = random.randint(1, 5)
    if traffic_type == 1:
        print("HTTP")
        generate_http_traffic()            
    elif traffic_type == 2:
        print("HTTPS")
        generate_https_traffic()
            
    elif traffic_type == 3:
        print("SSH")
        generate_ssh_traffic()
            
    elif traffic_type == 4:
        print("SMTP")
        generate_mail_traffic()
    elif traffic_type == 5:
        print("FTP")
        generate_ftp_traffic()

        
fake = Faker()

# Tiempo de ejecución deseado en segundos
tiempo_deseado = 120

# Tiempo de inicio
tiempo_inicio = time.time()
if __name__ == "__main__":
    traffic_interval = 0 # tiempo entre cada generación de tráfico, en segundos
    while time.time() - tiempo_inicio < tiempo_deseado:       
        
        generate_traffic()
        time.sleep(traffic_interval) 
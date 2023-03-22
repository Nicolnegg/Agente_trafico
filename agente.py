from scapy.layers.http import HTTPRequest
from faker import Faker
from scapy.all import *

import requests
import time
import random
import paramiko


def getHttp(dst_ip):

    # Construir el paquete HTTP GET
    http_request1 = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=80)/HTTPRequest(Method='GET', Path='/')

    # Enviar el paquete
    print("Get http")
    sendp(http_request1)

def postHttp(dst_ip):
    # Construir el paquete HTTP POSt
    http_request2 = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=80)/HTTPRequest(Method='POST', Path='/', Host=dst_ip)
    print("Post http")
    # Enviar el paquete
    sendp(http_request2)

def putHttp(dst_ip):  
    # Construir el paquete HTTP POSt
    http_request3 = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=80)/HTTPRequest(Method='PUT', Path='/', Host=dst_ip)
    print("Put http")
    # Enviar el paquete
    sendp(http_request3)

def deleteHttp(dst_ip):   
    # Construir el paquete HTTP POSt
    http_request4 = scapy.all.Ether()/scapy.all.IP(dst=dst_ip)/scapy.all.TCP(dport=80)/HTTPRequest(Method='DELETE', Path='/', Host=dst_ip)
    print("Delete http")
    # Enviar el paquete
    sendp(http_request4)

def generate_http_traffic(tiempo_deseado):
    # Tiempo de inicio
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < tiempo_deseado: 
        # Crear una lista con las funciones y sus respectivas probabilidades
        funciones = [getHttp, postHttp, putHttp, deleteHttp]
        probabilidades = [0.6, 0.2, 0.1, 0.1]

        # Elegir una función con las probabilidades específicas
        funcion_elegida = random.choices(funciones, probabilidades)[0]
        #ip
        dst_ip = fake.ipv4_private()
        # Llamar a la función elegida
        funcion_elegida(dst_ip)
        # time.sleep(10) 
        #filtro http

def getHttp(url):
    myobj = {'somekey': 'somevalue'}
    x = requests.post(url, json = myobj)
def generate_https_traffic():

    url = fake.url()
    tiempo_inicio = time.time()
    tiempo_deseado=100
    while time.time() - tiempo_inicio < tiempo_deseado: 
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
tiempo_deseado = 1

# Tiempo de inicio
tiempo_inicio = time.time()
if __name__ == "__main__":
    traffic_interval = 0 # tiempo entre cada generación de tráfico, en segundos
    while time.time() - tiempo_inicio < tiempo_deseado:       
        
        generate_http_traffic()
        time.sleep(traffic_interval) 
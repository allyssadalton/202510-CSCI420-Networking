# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket

listen_port = 5555   # make sure > 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind( ('0.0.0.0', listen_port))

while True:
	print("Waiting for message")

	(msg, addr) = s.recvfrom(1000000)
	msg = msg.decode('UTF-8')
	print(f"{addr}: Len {len(msg)}")

	msg = str(len(msg))

	s.sendto(msg.encode('UTF-8'), addr)
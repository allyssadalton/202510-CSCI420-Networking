# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket

listen_port = 5555   # make sure > 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind( ('0.0.0.0', listen_port))

clients = {}

while True:
	print("Waiting for message")

	(msg, addr) = s.recvfrom(1024)
	msg = msg.decode('UTF-8')
	print(f"{addr}: {msg}")

	clients[addr] = 1

	if len(msg) == 0:
		continue

	if msg == "users?":
		s.sendto((str(clients)).encode('UTF-8'), addr)
		continue

	for c in clients.keys():
		s.sendto(msg.encode('UTF-8'), c)
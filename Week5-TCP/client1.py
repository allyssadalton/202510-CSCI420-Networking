# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket

port = 5555
#ip_server = "127.0.0.1"
ip_server = "10.100.93.164"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

while True:
	message = input("How many bytes to send")

	message = "a" * int(message)
	binary = message.encode('UTF-8')
	print(f"Bytes: {len(binary)}")

	s.sendto(binary, (ip_server, port))

	print("Message sent!")

	(msg, addr) = s.recvfrom(1024)
	msg = msg.decode('UTF-8')
	print(msg)
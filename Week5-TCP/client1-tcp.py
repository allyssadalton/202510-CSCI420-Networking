# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket

port = 5555
#ip_server = "127.0.0.1"
ip_server = "10.100.93.164"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect( (ip_server, port) )
	print("Connected to server")

	while True:
		message = input("What message to send?")

		s.sendall(message.encode('UTF-8'))

		print("Message sent!")

		(msg) = s.recv(1024)
		msg = msg.decode('UTF-8')
		print(msg)

print("Disconnected from server")
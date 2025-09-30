# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket, threading

port = 5555
#ip_server = "127.0.0.1"
ip_server = "10.100.93.164"

def listen(s):
	while True:
		msg = s.recv(1024)
		msg = msg.decode('UTF-8')
		print(msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect( (ip_server, port) )
	print("Connected to server")
	thread = threading.Thread(target=listen, args=[s]).start()

	while True:
		message = input("What message to send?")

		s.sendall(message.encode('UTF-8'))

print("Disconnected from server")
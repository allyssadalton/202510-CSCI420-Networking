# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket

listen_port = 5555   # make sure > 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ('0.0.0.0', listen_port))
	s.listen(0)
	print("Server waiting for connect")

	while True:
		client_socket, addr = s.accept()
		print(f"Got connect from {addr}")

		while True:
			print("Waiting for message")

			msg = client_socket.recv(1000000)
			msg = msg.decode('UTF-8')
			print(f"{addr}: Len {len(msg)}")

			msg = msg + " there is more"

			client_socket.sendall(msg.encode('UTF-8'))
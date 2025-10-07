# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket, threading

listen_port = 5555   # make sure > 1024

def TCPWorker(client_socket):
	while True:
			print("Waiting for message")

			msg = client_socket.recv(1000000)
			msg = msg.decode('UTF-8')
			print(f"{addr}: Len {len(msg)} {msg}")

			msg =msg + " nothing"

			client_socket.sendall(msg.encode('UTF-8'))
	print("TCP worker died")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ('0.0.0.0', listen_port))
	s.listen(0)
	

	while True:
		print("Server waiting for connect")
		client_socket, addr = s.accept()
		print(f"Got connect from {addr}")
		threading.Thread(target=TCPWorker, args=[client_socket]).start()

		
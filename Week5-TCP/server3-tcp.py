# Networking - CSCI 420
# Paul Talaga
# Sept 29, 2025
# TCP server demo

import socket, threading, pickle

listen_port = 5555   # make sure > 1024

def TCPWorker(all_sockets, client_addr):
	try:
		while True:
				print("Waiting for message")

				msg = all_sockets[client_addr].recv(1000000)
				if len(msg) == 0:
					del all_sockets[client_addr]
					return
				#msg = msg.decode('UTF-8')
				decoded = pickle.loads(msg)
				if 'fname' in decoded.keys():
					print(f"File from {decoded['username']} Len {len(msg)} ")
				else:
					print(f"Len {len(msg)} {decoded}")

				
				addresses = list(all_sockets.keys())

				for addr in addresses:
					try:
						all_sockets[addr].sendall(msg)
					except Exception as e:
						print(f"Exception {e}")
						del all_sockets[addr]
						continue
	except Exception as e:
		print(f"Exception {e}")
	print("TCP worker died")
	if client_addr in all_sockets.keys():  
		del all_sockets[client_addr]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ('0.0.0.0', listen_port))
	s.listen(0)
	sockets = {}	

	while True:
		print("Server waiting for connect")
		client_socket, addr = s.accept()
		sockets[addr] = client_socket
		print(f"Got connect from {addr}")
		threading.Thread(target=TCPWorker, args=[sockets, addr]).start()
	s.close()
		
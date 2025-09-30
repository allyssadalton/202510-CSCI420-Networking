# Networking - CSCI 420
# Paul Talaga
# Sept 9, 2025
# UDP client/server demo

import socket, threading

listen_port = 5555   # make sure > 1024

def TCPWorker(all_sockets, client_addr):
	try:
		while True:
				print("Waiting for message")

				msg = all_sockets[client_addr].recv(1000000)
				msg = msg.decode('UTF-8')
				print(f"Len {len(msg)} {msg}")

				
				addresses = list(all_sockets.keys())

				for addr in addresses:
					try:
						all_sockets[addr].sendall(msg.encode('UTF-8'))
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
		
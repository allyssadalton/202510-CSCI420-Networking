# Networking - CSCI 420
# Paul Talaga
# Sept 29, 2025
# TCP client/server demo with file saving functionality
# Note this will NOT handle large files as it loads the file into memory.

import socket, threading, pickle

port = 5555
#ip_server = "127.0.0.1"
ip_server = "10.100.233.251"

def listen(s):
	while True:
		data = s.recv(1000000)	# Only tested through localhost.  May not work on real network
		data = pickle.loads(data)
		if 'fname' in data.keys():	# Detect if a file is sent based on if a key is in the dictionary
			# Getting a file!
			print(f"Getting {data['fname']} from {data['username']} {len(data['file'])} bytes")
			with open("new-" + data['fname'], 'wb') as f:
				f.write(data['file'])
			print("File saved!")
		else:
			msg = f"{data['username']}: {data['msg']}"
			print(msg)


username = input("What is your username?")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect( (ip_server, port) )
	print("Connected to server")
	thread = threading.Thread(target=listen, args=[s]).start()

	while True:
		message = input("What message to send or a file to send?")
		if ".png" in message or ".jpg" in message or ".py" in message:
			with open(message, "rb") as f:
				file_data = f.read()
			data = pickle.dumps({'msg': message, 'username': username, 'fname':message, 'file': file_data})
		else:

			data = pickle.dumps({'msg': message, 'username': username})

		s.sendall(data)

print("Disconnected from server")
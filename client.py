# File: client.py
# Name: Allyssa Dalton
# Date September 17th, 2025
import socket
import threading

server_ip = "127.0.0.1"
server_port = 5558
name = input("Enter your display name: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(f"/register {name}".encode("utf-8"), (server_ip, server_port))

def Listen():
    while True:
        try:
            msg, _ = client_socket.recvfrom(1024)
            print("\n" + msg.decode("utf-8"))
        except:
            break

threading.Thread(target=Listen, daemon=True).start()

while True:
    message = input(f"{name} > ").strip()
    if message.lower() == "/quit":
        break
    client_socket.sendto(message.encode("utf-8"), (server_ip, server_port))

client_socket.close()
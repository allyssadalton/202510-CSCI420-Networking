# File: server.py
# Name: Allyssa Dalton
# Date September 17th, 2025
import socket
from datetime import datetime

listen_port = 5558
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', listen_port))

people = {}
names = set()

def Register(address, name):
    if name in names:
        server_socket.sendto("Name is already in use. Try again, loser. (Haha, just joking dawg.)".encode('UTF-8'), address)
        return False
    people[address] = name
    names.add(name)
    print(f"[{CurrentTime()}] {name} has joined the chat!")
    Broadcast(f"[{CurrentTime()}] {name} has joined the chat!")
    return True

def ListPeople(requesterAddress):
    peopleList = ", ".join(people.values())
    server_socket.sendto(f"Current users: {peopleList}".encode("utf-8"), requesterAddress)

def PrivateMessage(senderAddress, message):
    parts = message.split(" ", 2)
    if len(parts) < 3:
        server_socket.sendto(
            "Usage: /message <user> <text>".encode("utf-8"), senderAddress
        )
        return
    targetName, messageText = parts[1], parts[2]
    targetAddress = None    
    for address, displayName in people.items():
        if displayName == targetName:
            targetAddress = address
            break
    if not targetAddress:
        server_socket.sendto(f"User '{targetName}' not found.".encode("utf-8"), senderAddress)
        return
    senderName = people[senderAddress]
    formatted = f"[{CurrentTime()}] (private) {senderName} -> {targetName}: {messageText}"
    server_socket.sendto(formatted.encode("utf-8"), targetAddress)
    server_socket.sendto(formatted.encode("utf-8"), senderAddress)

def CurrentTime():
    return datetime.now().strftime("%H:%M:%S")

def Broadcast(message, exclude=None):
    for address in people:
        if address != exclude:
            server_socket.sendto(message.encode("utf-8"), address)

while True:
    message, address = server_socket.recvfrom(1024)
    message = message.decode('UTF-8').strip()
    
    if not message:
        continue
    
    if message.startswith("/register "):
        username = message.split(" ", 1)[1]  
        if address not in people:
            if not Register(address, username):  
                continue 
        continue  

    if address not in people:
        server_socket.sendto("Please register first with original display name".encode("utf-8"), address)
        continue
    
    if message.lower() == "/who":
        ListPeople(address)
    elif message.lower().startswith("/message "):
        PrivateMessage(address, message)
    else:
        senderName = people[address]
        fullMessage = f"[{CurrentTime()}] {senderName}: {message}"
        print(f"{address}: {fullMessage}")
        Broadcast(fullMessage)
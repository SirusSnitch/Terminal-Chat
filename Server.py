#!/usr/bin/env python3

import socket
import threading

HOST = "127.0.0.1"
PORT = 4000  
clients = []  

def handle_client(client, addr):
    print(f"New connection: {addr}")
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg or msg.lower() == "exit":
                break
            print(f"{addr}: {msg}")
            broadcast(msg, client)
        except:
            break
    clients.remove(client)
    client.close()

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {PORT}...")
while True:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()

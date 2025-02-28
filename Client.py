#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
SERVER_PORT = 4000

username = input("Enter your name: ")
SEND_PORT = int(input("Enter your sending port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.bind(("", SEND_PORT)) 
client.connect((HOST, SERVER_PORT))

while True:
    msg = input(f"{username}: ")
    client.send(f"{username}: {msg}".encode())
    if msg.lower() == "exit":
        break

client.close()

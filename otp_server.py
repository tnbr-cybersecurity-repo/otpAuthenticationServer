#!usr/bin/env python3

# Accept Input for Username and Password
# Encrypt Password Input
# Compare against /etc/shadow
# Validate if Input exist in /etc/shadow

from socket import socket, AF_INET, SOCK_STREAM
import threading
from colorama import Fore as Colors
from otpGenerator import generator, passwords



generator('0810770FF00FF07012')

password = passwords


def server_connection(SERVER_IP, SERVER_PORT):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5)
    print(f"\n[*] Server Listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Waiting for a connection to come in
        client, addr = server.accept()
        client.send("I am the server accepting connections...".encode())
        handle_client(client)
        print(
            f"[*] Accepted connection from: " + Colors.GREEN + f"{addr[0]}" + Colors.RESET + ":" + Colors.LIGHTBLUE_EX +
            f"{addr[1]}" + Colors.RESET)

        client.close()


def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print(f"[*] Received request : {request} from client {client_socket.getpeername()}")
        handle_otp(request)
        client_socket.sendall(bytes("ACK", "utf-8"))
        if request == 'quit':
            client_socket.close()


def handle_otp(request):
    for otp in range(0, password.__len__()):
        found = password[otp] == request
        if found:
            return "access granted"
        else:
            return "denied message"


# Initiate the Server Connection
server_connection('127.0.0.1', 9997)
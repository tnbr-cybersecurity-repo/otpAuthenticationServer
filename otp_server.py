#!usr/bin/env python3

# Accept Input for Username and Password
# Encrypt Password Input
# Compare against /etc/shadow
# Validate if Input exist in /etc/shadow

from socket import socket, AF_INET, SOCK_STREAM
from colorama import Fore as Colors
from otpGenerator import generator, passwords

password = passwords


# Function to start Server Listening on designated port
def server_connection(SERVER_IP, SERVER_PORT):
    # Establish Server Family and Connection Type
    server = socket(AF_INET, SOCK_STREAM)
    # Bind Server to Address
    server.bind((SERVER_IP, SERVER_PORT))
    # Server will facilitate up to 5 connections
    server.listen(5)
    print(f"\n[*] Server Listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Waiting for a connection to come in
        client, addr = server.accept()
        # Confirm to remote device a successful connection made
        client.send("I am the server accepting connections...".encode())

        handle_client(client)
        print(
            f"[*] Accepted connection from: " + Colors.GREEN + f"{addr[0]}" + Colors.RESET + ":" + Colors.LIGHTBLUE_EX +
            f"{addr[1]}" + Colors.RESET)

        client.close()


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[*] Received request : {request} from client {client_socket.getpeername()}")

    while password.__len__() <= 10:
        # Handles Incoming Request
        for otp in range(0, password.__len__()):
            found = password[otp] == request
            if found:
                break
        if found:
            client_socket.sendall(bytes("ACK", "utf-8"))
            print("access granted")
        else:
            print("denied message")

    client_socket.close()


# Generate OTP Hex Values
generator('0810770FF00FF07012', 3)

# Initiate the Server Connection
server_connection("127.0.0.1", 8888)

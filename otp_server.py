#!usr/bin/env python3

# Accept Input for Username and Password
# Encrypt Password Input
# Compare against /etc/shadow
# Validate if Input exist in /etc/shadow

from socket import socket, AF_INET, SOCK_STREAM
from colorama import Fore as Colors
from otpGenerator import generator, passwords

password = passwords

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9998

# Generate OTP Hex Values
generator('0810770FF00FF07012', 8)
print(password)
# Define Server Family as Internet and Connection Type as TCP
server = socket(AF_INET, SOCK_STREAM)

# Bind Server to Address
server.bind((SERVER_IP, SERVER_PORT))

# Server will facilitate up to 5 connections
server.listen(5)

print(f"\n[*] Server Listening on " + Colors.GREEN + f"{SERVER_IP}" + Colors.RESET + ":" + Colors.LIGHTBLUE_EX +
      f"{SERVER_PORT}" + Colors.RESET)

# Waiting for a connection to come in
client, addr = server.accept()

# Confirm to remote device a successful connection made
client.send("I am the server accepting connections...".encode())
print(
    f"[*] Accepted connection from: " + Colors.GREEN + f"{addr[0]}" + Colors.RESET + ":" + Colors.LIGHTBLUE_EX +
    f"{addr[1]}" + Colors.RESET)


def handle_client(client_socket):
    request = client_socket.recv(1024).decode()

    print(f"[*] Received request : {request} from client {client_socket.getpeername()}")

    # Handles Incoming Request
    for otp in range(0, password.__len__()):
        plsfind = password[otp] == str(request)
        if plsfind:
            print(f'Found is:{plsfind}')
            break
    if plsfind:
        client_socket.sendall("ACK - Access Granted".encode())
        print("Access Granted")
    else:
        client_socket.sendall(bytes("ACK - Access Denied".encode()))
        print("Access Denied")


while True:
    handle_client(client)

server.close()

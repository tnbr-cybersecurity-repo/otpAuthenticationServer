#!usr/bin/env python3
from random import random
import socket
from colorama import Fore as Colors
from otpGenerator import generator, passwords
import random

generator('0810770FF00FF07012')

password = passwords


def client_connection(host, port):
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((host, port))
        print(f'Connected to host {str(host)} in port: {str(port)}')
        message = mysocket.recv(1024)
        print(f"Message received from the server: {message}")

        message = random.choice(password)
        mysocket.send(bytes(message.encode('utf-8')))
        for otp in range(0, password.__len__()):
            found = password[otp] == message
            if found:
                break
        password.pop(otp)



    except socket.error as error:
        print("Socket error " + Colors.LIGHTRED_EX + f"{error}" + Colors.RESET)
    finally:
        mysocket.close()


client_connection(host="127.0.0.1", port=9997)

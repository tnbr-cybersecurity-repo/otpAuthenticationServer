#!usr/bin/env python3
import time
from random import random
import socket
from colorama import Fore as Colors
from otpGenerator import generator, passwords
import random

password = passwords


def client_connection(host, port):
    print(password)
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((host, port))
        print(f'Connected to host {str(host)} in port: {str(port)}')
        message = mysocket.recv(1024)
        print(f"Message received from the server: {message}")

        while password.__len__() > 0:
            # Randomly select OTP from list
            message: hex = random.choice(password)
            print(f'Print the OTP selected: {message}')
            # while True:
            for otp in range(password.__len__()):
                found = password[otp] == message
                if found:
                    break
            if found:
                mysocket.send(bytes(message.encode('utf-8')))
                password.pop(otp)
                print(f'Print the updated Password List\n{password}')
                time.sleep(3)
            else:
                message = [] | message == 'quit'
                mysocket.send(bytes(message.encode('utf-8')))
                print(message)
                break


    except socket.error as error:
        print("Socket error " + Colors.LIGHTRED_EX + f"{error}" + Colors.RESET)
    finally:
        mysocket.close()


# Generate OTP Hex Values
generator('0810770FF00FF07012', 10)

# Start the Client Connection
client_connection("127.0.0.1", 9998)

import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the hostname of the server :"))
port = 8080
s.connect((host,port))
print("Connected to chat server ")
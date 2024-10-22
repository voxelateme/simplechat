import socket
from _thread import *

cl_socket = socket.socket()
cl_socket.connect(('192.168.126.186', 55013))  # Server IPv4


def input_thread(cl_socket):
    while True:
        output = cl_socket.recv(1024)
        print(output.decode())


while True:
    start_new_thread(input_thread, (cl_socket,))
    msg = input()
    if msg:
        cl_socket.send(msg.encode())
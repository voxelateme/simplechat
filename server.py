import socket
from _thread import *

bufsize = int(input("Type bufsize: "))  # buffer size
server = socket.socket()
port = 55013
server.bind(('192.168.126.186', port))  # IPv4 from ipconfig
server.listen(10)

print("Chat server successfully started.")


def client_thread(con):
    print("Client connected")
    while True:
        try:
            data = con.recv(bufsize)
        except:
            print("No data! Client disconnect initiated")
            con.close()
            client_list.remove(con)
            break
        if data:
            message = data.decode()
            print(f"Client sent: {message}")
            for clients in client_list:
                if clients == con:
                    continue
                print("Sending data to client")
                return_message = ('Server Message: ' + message).encode()
                clients.send(return_message)


client_list = list()
while True:
    con, _ = server.accept()
    client_list.append(con)
    print(len(client_list))
    start_new_thread(client_thread, (con,))
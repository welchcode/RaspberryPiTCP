import socket
import sys

print("-------------------------------------------------------------")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 7500)

sock.bind(server_address)

sock.listen(1)

while True:
    print("Listening")
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)

    data = connection.recv(8000)
    print(data.decode())





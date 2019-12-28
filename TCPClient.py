import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = "I am the client"

client.connect(('localhost', 7500))
client.sendto(message.encode(), ('localhost', 7500))

client.close()
import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(len(sys.argv) == 2):
    message = str(sys.argv[1])
else:
    message = 'Arg length of ' + str(len(sys.argv)) + ' is not correct, arg length must be exactly 2 ---> the first arg is the script, and the second is the message'

#raspberryPi's IP on the network
server_hostname = '192.168.1.12'

client.connect((server_hostname, 7500))
client.sendto(message.encode(), (server_hostname, 7500))

client.close()
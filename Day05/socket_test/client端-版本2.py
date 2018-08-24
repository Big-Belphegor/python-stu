__author__ = "Alien"
import socket
client = socket.socket()
client.connect(('localhost',9000))

while True:
    n = input('>>:').split()
    client.send(n)
    data = client.recv(1024)
    print(data.decode())

client.close()
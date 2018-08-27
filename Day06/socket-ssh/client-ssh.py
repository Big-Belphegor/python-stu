__author__ = "Alien"
import socket
client = socket.socket()

client.connect(('localhost',6666))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print('Total transmission:',cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print('Transferred size:',received_size)
        print(received_data.decode())

client.close()


__author__ = "Alien"
import socket,os
server = socket.socket()

server.bind(('localhost', 9000))
server.listen()
print('Wating for you...')

while True:
    conn,addr = server.accept()
    print('来电了！')

    while True:
        data = conn.recv(1024)
        print('recv:',data)
        if not data:
            break
        # res = os.popen(data).read()       # 打印系统命令
        conn.send(data.upper())

server.close()
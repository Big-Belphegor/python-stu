__author__ = "Alien"
import socket,os
server = socket.socket()

server.bind(('localhost',6666))
server.listen()

while True:
    conn,addr = server.accept()
    print('IP address:',addr)

    while True:
        print('Client connection...')
        data = conn.recv(1024)
        if not data:
            print('Client disconnect!')
            break
        cmd_res = os.popen(data.decode()).read()        # 接受字符串命令，返回结果也是字符串
        print('Total transmission:',len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "Not Output!"

        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        conn.send(cmd_res.encode('utf-8'))
        print('Over')

server.close()

__author__ = "Alien"
# 要求：
# 1、实现主机批量连接
# 2、能够对主机进行批量cmd操作
# 3、根据用户名和密码区分

import paramiko,threading
import group1,group2



class all(object):
    def __init__(self,groupname):
        self.groupname = groupname
        # self.hostIP = []
        # self.username = []
        # self.password = []

    def check_host(self):
        for x in self.groupname.host:
            print('主机名称：%s ' % x)
        print('主机个数：%s' % len(self.groupname.host))

    # def __host__(self):
    #     for x,y in self.groupname.pwn:
    #         self.username = x
    #         self.password = y

    def ssh_client_cmd(self,port,username,password,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.groupname,port=port,username=username,password=password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print(result.decode())
        ssh.close()

    def ssh_client_scp(self,port,username,password):
        transport = paramiko.Transport((self.groupname, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        num = input('''
        1. Put
        2. Get
        >>:
        ''').strip()
        if num == '1':
            s_path = input('上传文件路径：').strip()
            d_path = input('保存文件路径：').strip()
            sftp.put(s_path,d_path)
        elif num == '2':
            s_path = input('下载文件路径：').strip()
            d_path = input('保存文件路径：').strip()
            sftp.get(s_path,d_path)
        else:
            print('输入错误！')

obj = input('''
1. 查询主机信息
2. CMD远程主机
3. Put/Get文件
''')
if obj == '1':
    all.check_host('group1')




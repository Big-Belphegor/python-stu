__author__ = "Alien"
# SSH-连接(无Key版)
import paramiko
# # 实例化ssh客户端
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       # 跳过Key认证
# # 连接远程节点
# ssh.connect(hostname='192.168.181.155',port=22,username='test',password='123123')
# # 执行命令
# stdin,stdout,stderr = ssh.exec_command('df')    # stdin:标准输入；stdout:标准输出;stderr:标准错误
# # 获取命令结果
# result = stdout.read()
# print(result.decode())
# # 关闭连接
# ssh.close()

# SSH连接(Key验证版本)
# ssh2 = paramiko.SSHClient()
# private_key = paramiko.RSAKey.from_private_key_file('id_rsa_88')                    # 导入私钥
# ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh2.connect(hostname='192.168.181.155',port=22,username='root',pkey=private_key)   # 认证私钥
# stdin,stdout,stderr = ssh2.exec_command('df')
# result = stdout.read()
# print(result.decode())

# SSH-SCP
transport = paramiko.Transport(('192.168.181.155',22))      # 与服务器建立连接
transport.connect(username='test',password='123123')        # 连接传输用户

sftp = paramiko.SFTPClient.from_transport(transport)        # 建立文件传输通道
# 上传文件，格式：xxx.put('本地文件路径+文件名' ‘远程文件路径’)
sftp.put('C:\\Users\\dxw-user\\Desktop\\01.png','/home/test/01.png')
# 下载文件，格式：xxx.get('远程文件路径' ‘本地保存路径+文件名’)
sftp.get('/home/test/tt','C:\\Users\\dxw-user\\Desktop\\tt_new')
transport.close()



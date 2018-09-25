__author__ = "Alien"
import hashlib

md5 = hashlib.md5()         # 实例化一个md5
print(md5)

md5.update('Hello world'.encode('utf-8'))       # 添加要加密的字符串
print(md5.hexdigest())                          # 获取加密的字符串

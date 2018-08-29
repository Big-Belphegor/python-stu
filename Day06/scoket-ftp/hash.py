__author__ = "Alien"
import hashlib

m = hashlib.md5()
m.update(b'test')

# print(m.digest())     # 16进制版
print(m.hexdigest())    # 二进制版

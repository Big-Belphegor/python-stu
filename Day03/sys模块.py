__author__ = "Alien"
import sys
print(sys.argv)     # 获取当前模块

# print(sys.exit())   # 退出程序
print(sys.path)     # 返回模块的搜索路径
print(sys.platform) # 返回系统名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
print(val)
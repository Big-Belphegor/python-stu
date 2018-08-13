__author__ = "Alien"

# 时间模块
import time,datetime

# print(time.time())                  # 时间戳，以秒为单位
# print(time.localtime())             # 将本地当前时间戳转为时间组
# print(time.gmtime(1820455584))      # 将自定义时间戳转换为时间组
#
# print(time.timezone)                # 时区
# a = -28800/3600                     # 中国在东八区(UTC-8)，所以是-8.0
# print(a)
#
# x = time.localtime()                # 获取时间组中某个值
# print(x)
# print(x.tm_yday)
#
# print(time.mktime(x))               # 将时间组转换为时间戳
#
# print(time.strftime("%y-%m-%d %H:%M:%S"))                       # 将当前时间转为字符串
# print(time.strptime("18-08-10 14:56:30",'%y-%m-%d %H:%M:%S'))   # 将时间字符串转为时间元组

# print(datetime.datetime.now())        # 查看当前时间

# 随机模块
import random
# print(random.randint(1,5))              # 随机1-5之间的数
# print(random.randrange(5))              # 随机0-4之间的数
# print(random.choice('hello'))           # 从后面的值中随机打印一个(可以是元组、列表)
# print(random.choice([1,2,3,4]))         # 从后面的值中随机打印一个(可以是元组、列表)
#
# print(random.uniform(1,5))              # 1-5区间内随机打印
#
# tt = [1,2,3,4,5]
# random.shuffle(tt)                      # 打乱原有顺序，每次都不一样(洗牌功能)
# print(tt)

# 小实例：随机打印4个数字
# changenum = ''
#
# for i in range(4):
#     num1 = random.randrange(0,4)
#     if i == num1:
#         tmp = chr(random.randint(10,20))    # 转为字母
#     else:
#         tmp = random.randint(0,9)
#     changenum += str(tmp)+' '
#
# print(changenum)

# os模块
import os

# print(os.getcwd())              # 获取当前路径
#
# os.chdir("C:\Desktop")          # 切换目录
# os.curdir                       # 等同Linux的.
# os.pardir                       # 等同Linux的..
# os.makedirs("C:\\a\\b\\c")      # 递归创建目录
# os.removedirs("Path")           # 递归删除‘空’目录
#
# os.mkdir("Path")                # 单独创建目录
# os.rmdir("Path")                # 删除指定目录

# print(os.listdir('..'))         # 等同Linux的ls
# os.remove()                     # 移除一个文件
# os.rename()                     # 重命名目录/文件
# print(os.stat('test'))          # 获取目录/文件信息

# print(os.sep)                   # 查看当前平台的路径分隔符
# print(os.linesep)               # 打印当前系统的换行符
# print(os.environ)               # 打印环境变量
# print(os.name)                  # 系统名

# sys模块
# import sys
# print(sys.argv)                 # 获取参数
# print(sys.version)              # 版本

# shutil模块
import shutil

# f1 = open("01.py",encoding="utf-8")
# f2 = open("02",'w',encoding="utf-8")
# shutil.copyfileobj(f1,f2)       # 拷贝f1到f2文件，注意：文件编码要一直
#
# shutil.copyfile("01.py","03")   # 拷贝01.py到03文件，注意：该方法不需要提前创建文件

# shutil.copymode(src,dat)        # 只拷贝源文件的权限
# shutil.copytree("test1","test2")    # 递归拷贝目录
# shutil.rmtree("test2")              # 删除递归目录
# shutil.move(src,dat)                # 移动递归文件
# shutil.make_archive("压缩包","zip","F:\python-stu\Day01")      # 当前目录下创建压缩包(压缩整个目录)，格式：包名+压缩形式+被压缩文件路径


# import zipfile
#
# z = zipfile.ZipFile("压缩包2.zip",'w')     # 压缩单独/个别文件
# z.write("01.py")
# z.close()
#
# z = zipfile.ZipFile("压缩包2.zip",'r')     # 解压刚才的包
# z.extractall()
# z.close()

import shelve
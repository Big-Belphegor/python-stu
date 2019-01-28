__author__ = "Alien"
import os

# os.makedirs('test\\t1')       # 递归创建目录
# os.removedirs('test\\t1')     # 递归删除目录

# os.mkdir('h1')             # 创建一个目录
# os.rmdir('h1')             # 删除一个目录

# os.remove('filename')      # 删除一个文件

# os.rename('oldfilename','newfilename')      # 为文件/目录重命名

# a = os.listdir(r'/var/log/')    # 打印指定目录下文件
# print(a)                        # 注意：r代表标识后面的字符串为原生字符串，不需要转义

# b = os.stat('/root/001')        # 获取文件详细信息
# print(b)
# print(b.st_atime)               # 获取文件的最后一次访问时间

# c = os.sep                      # 获取当前系统的路径分割符
# print(c)
#
# print(os.system('dir'))                 # 执行系统命令
# print(os.environ)                       # 获取环境变量
# print(os.path.abspath('./复习.py'))      # 获取某个文件的绝对路径
# print(os.path.split('F:\python-stu\Day03\复习.py'))      # 将路径进行分割为文件路及文件名
# print(os.path.dirname('F:\python-stu\Day03\复习.py'))    # 分割出该绝对路径的目录
# print(os.path.exists('复习.py'))                         # 判断path是否存在
# print(os.path.isabs('F:\python-stu\Day03\复习.py'))      # 判断path是否为绝对路径
# print(os.path.isfile('F:\python-stu\Day03\\复习.py'))    # 判断文件是否存在
# print(os.path.isdir('F:\python-stu\Day03'))             # 判断目录是否存在
print(os.path.join('my','\\name','\\is','Alien'))       # 合并路径
print(os.path.getatime('复习.py'))                       # 获取目录或文件的最后存取时间
print(os.path.getmtime('复习.py'))                       # 获取目录或文件的最后修改时间


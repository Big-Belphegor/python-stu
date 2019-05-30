__author__ = "Alien"
# # os模块
# import os

# print(os.curdir)    # 获取当前目录，等于'.'
# print(os.pardir)    # 获取父级目录，等于'..'
# os.chdir('..')      # 更改当前工作目录，类似'cd'命令
# print(os.getcwd())  # 获取当前工作目录

# os.mkdir('test_dir1')                 # 创建目录
# os.makedirs('test_dir2\\t1')          # 递归创建目录
# os.rmdir('test_dir1')                 # 删除目录
# os.removedirs('test_dir2\\t1')        # 递归删除目录
# os.remove('file1')                    # 删除一个文件

# a = os.listdir('F:\ChromeDownloader')   # 将指定目录下文件存储到列表
# for i in a:
#     print(i)

# with open('test1','w') as f:
#     pass
# os.rename('test1','new_test1')          # 修改文件名

# a = os.stat('.\\login.py')          # 显示指定文件/目录的详细信息
# print(a.st_size)                    # 可以通过赋值取出指定的信息

# print(os.sep)       # 获取当前系统的分隔符样式，windows下是'\'，Linux下是'/'，当不确定系统版本时用其在代码中代替。
# print(os.linesep)   # 同上，区分'\r\n'与'\n'
# print(os.pathsep)   # 同上，区分';'
# a = os.path.sep.join(['dirname1','filename1'])        # 将dirname1和filename1拼接为适用于当前系统的路径
# print(a)

# print(os.name)              # 显示平台名称，nt=windows，posix=Linux
# print(os.system('dir'))     # 系统命令

# print(os.environ)                                           # 当前环境变量
# print(os.path.abspath('.\\login.py'))                       # 获取指定文件的绝对路径
# print(os.path.split('F:\python-stu\jd_test\login.py'))      # 分隔绝对路径的路径与文件名
# print(os.path.dirname('F:\python-stu\jd_test\login.py'))    # 获取login.py的上层目录绝对路径

# print(os.path.getmtime('login.py'))     # 获取文件/目录最后的修改时间
# print(os.path.getatime('login.py'))     # 获取文件/目录最后的存取时间


# # sys模块
# import sys

# a = sys.argv[1]             # 外部传参函数，默认是连文件名一起以列表形式输出
# if a == 'pull':
#     print('pulling' )
# else:
#     print('Pushing')

# print(sys.path)             # 寻找模块的绝对路径
# print(sys.platform)         # 平台及位数

# # hashlib模块(加密模块)
# import hashlib
#
# x = hashlib.md5()       # 声明一个加密实例
# x.update(b'abc')        # 添加加密信息
# print(x.hexdigest())    # 按需指定进制并打印

# logging模块
import logging

# # 日志级别
# logging.debug('=== Trigger Debug ===')
# logging.info('=== Trigger Info ===')
# logging.warning('=== Trigger Warning ===')
# logging.error('=== Trigger Error ===')
# logging.critical('=== Trigger Critical ===')

# # 自定义日志内容
# logging.basicConfig(level=logging.NOTSET,
#                     format='%(asctime)s %(name)s:%(levelname)s\t%(message)s',
#                     filename='test.log',
#                     filemode='w',
#                     datefmt='%Y/%m/%d - %H:%M:%S'
#                     )
# '''
# level 定义日志级别为NOTSET后所有级别都会被打印，举例：如果设置ERROR，则只会打印ERROR和CRITICAL级别的日志；
# format 定义日志格式，常用参数含义；
#     %(asctime)s：打印日志的时间
#     %(lineno)d：打印日志的当前行号
#     %(levelno)s：打印日志级别的数值
#     %(levelname)s：打印日志级别的名称
#     %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
#     %(filename)s：打印当前执行程序名
#     %(funcName)s：打印日志的当前函数
#     %(thread)d：打印线程ID
#     %(threadName)s：打印线程名称
#     %(process)d：打印进程ID
#     %(message)s：打印日志信息
# filename 定义日志文件的绝对路径；
# filemode 定义日志文件打开模式，'w'或'a'新建/追加
# datefmt 定义时间格式，用法同time.strftime()，其修改的时asctime的默认值；
# stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；
# '''
# x = logging.getLogger(__name__)         # 实例化一个对象，使用上面的logging模板
# x.debug('=== Trigger Debug ===')
# x.info('=== Trigger Info ===')
# x.warning('=== Trigger Warning ===')
# x.error('=== Trigger Error ===')
# x.critical('=== Trigger Critical ===')
# x.critical('=== Trigger Critical ===')
# x.critical('=== Trigger Critical ===')

# 同时在屏幕和文件生成日志内容
all_log = logging.getLogger()            # 定义总日志实例
fh = logging.FileHandler('test.log')    # 定义子对象，用于存放日志的文件
ch = logging.StreamHandler()            # 定义子对象，用于存放屏幕打印的日志
formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s\t%(message)s')    # 定义统一的日志格式，与上面的方法相同

fh.setFormatter(formatter)          # 添加日志格式给fh
ch.setFormatter(formatter)          # 添加日志格式给ch

all_log.addHandler(fh)               # 将两个子对象添加到logger总日志实例中
all_log.addHandler(ch)
all_log.setLevel(logging.DEBUG)      # 修改默认的日志级别

all_log.debug('xxxxxx')              # 测试，对all_log对象写入不同级别的日志
all_log.warning('xxxxxx')


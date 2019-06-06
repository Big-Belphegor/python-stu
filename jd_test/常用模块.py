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
# import logging

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
#
# # 同时在屏幕和文件生成日志内容
# all_log = logging.getLogger()            # 定义总日志实例
# fh = logging.FileHandler('test.log')    # 定义子对象，用于存放日志的文件
# ch = logging.StreamHandler()            # 定义子对象，用于存放屏幕打印的日志
# formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s\t%(message)s')    # 定义统一的日志格式，与上面的方法相同
#
# fh.setFormatter(formatter)          # 添加日志格式给fh
# ch.setFormatter(formatter)          # 添加日志格式给ch
#
# all_log.addHandler(fh)               # 将两个子对象添加到logger总日志实例中
# all_log.addHandler(ch)
# all_log.setLevel(logging.DEBUG)      # 修改默认的日志级别
#
# all_log.debug('xxxxxx')              # 测试，对all_log对象写入不同级别的日志
# all_log.warning('xxxxxx')
#
# # 更多的信息参考官网：https://docs.python.org/3.4/library/logging.html?highlight=logging#module-logging

# # ConfigParser模块，配置文件模块
# import configparser

# # 查看
# f1 = configparser.ConfigParser()                # 生成实例
# f1.read('mysql.conf',encoding="utf-8")          # 获取mysql.conf文件到f1对象
#
# print(f1.sections())                            # 获取所有section节点
# print(f1.options('mysqld'))                     # 获取指定option内的所有key
# print(f1.get('mysqld','datadir'))               # 获取指定option-key的值
# print(f1.items('mysqld'))                       # 获取指定option的所有数据

# # 增加
# f2 = configparser.ConfigParser()
#
# f2.add_section('test')
# f2['test'] = {
#     'Username':'Alien',
#     'Password':'123456'
# }
# with open('mysql.conf','a') as configfile:
#     f2.write(configfile)

# # 修改
# f3 = configparser.ConfigParser()
#
# f3.read('mysql.conf',encoding='utf-8')
# f3.set('test','Username','User1')                   # 修改test-Username的Value值
# f3.write(open('mysql.conf','w'))

# # 删除
# f4 = configparser.ConfigParser()
# f4.read('mysql.conf',encoding='utf-8')
# f4.remove_section("test")                   # 删除test这个section
# f4.remove_option('mysqld','log-bin')        # 删除指定option的key
# f4.write(open('mysql.conf','w'))

# # re模块，正则表达式
# import re

# # 简单的正则语言示例
# s = 'Hello world'
# print(s.find('l'))              # 查找匹配第一个字符的索引位置
# print(s.replace('ll','xx'))     # 替换字符
# print(s.split('w'))             # 指定分隔符

# # 正式开始介绍re模块
# # 格式：re.方法('匹配规则','被匹配的字符串')
# x = 'Hello world wxxl wxxxl'
# y = '18241877987'
# print(re.findall('H.l',x))          # '.'匹配任意单个字符，除换行符
# print(re.findall('^H...o',x))       # '^'匹配字符串首字符/字符串
# print(re.findall('w...l$',x))       # '$'匹配字符串尾字符/字符串
# print(re.findall('wx*',x))          # '*'匹配时其前面字符/字符串至少匹配0到n次
# print(re.findall('x+l',x))          # '+'匹配时其前面字符/字符串至少匹配1到n次
# print(re.findall('x?l',x))          # '?'匹配时其前面字符/字符串至少匹配0到1次
#
# print(re.findall('[0-9]{11}',y))    # '{}'匹配其前面字符/字符串出现'{}'内设定的次数，或次数范围
# print(re.findall('x{1,3}l',x))      # '{}'的次数范围示例
#
# print(re.findall('[r,x]l',x))            # '[]'匹配其内部设定的条件，符合便进行匹配
# print(re.findall('[^a,c]','abcefg'))     # '[^]'表示取反，注意该实例是取字符串内除了a和c的值
# print(re.findall('[a-z]','abc'))         # '[-]'表示取值范围，可以是0~9,A~Z等
#
# print(re.findall('\d','12345789'))                  # '\d'匹配所有数字字符，等同于[0-9]
# print(re.findall('\w','abc efg123'))                # '\w'匹配所有字符，等同于[0-9a-zA-Z]
# print(re.findall(r'I\b','Hello,I am Alien'))        # '\b'匹配其前面字符与其后字符中间的特殊字符(如：空格、$等)，注意使用时需要加'r'
# print(re.findall(r'\bam','Hello,I am Alien'))       # 此处又举例了一个特殊字符在匹配字符前的情况
# '''
# 正则表达式中其它特殊元字符：
# \d      # 匹配任何十进制数，等同于[0-9]
# \D      # 匹配任何非十进制数的字符，等同于[^0-9]
# \s      # 匹配任何空白字符，等同于[\t\n\r\f\v]
# \S      # 匹配任何空非白字符，等同于[^\t\n\r\f\v]
# \w      # 匹配任何字母数字字符，等同于[0-9a-zA-Z]
# \W      # 匹配任何非字母数字字符，等同于[^0-9a-zA-Z]
# \b      # 匹配一个单词的边界，也就是单词和空格的位置
# '''

# print(re.findall(r'\\e','abcd\e'))          # '\'转义符，将特殊元字符变为普通字符，也可以将部分普通字符变为特殊元字符，注意匹配其自身时需要加'r'
# print(re.findall('\\\\e','abcd\e'))         # '\'的另外一种匹配方式
#
# print(re.findall('(com|cn)','baidu.com'))         # '|'匹配两个中的一个，表示或的意思
# print(re.findall('(\+86)|(abc)','+86abcde'))      # '()'表示一个元素组，将多个字符变成一个整体去进行匹配


# # re模块的方法
# a = 'abcabcee\e'
# b = '2019-06-05 13:40'
# print(re.search('abc',a).group())           # 'search'方法匹配第一个符合规则的字符/字符串，返回一个第一个对象；注意：打印用.group()方法
# print(re.findall('abc',a))                  # 'findall'方法匹配所有符合规则的字符/字符串，返回一个列表
# print(re.match('abc',a).group())            # 'match'方法匹配开头符合规则的字符/字符串，返回一个对象，打印需要用.group()方法
# print(re.sub('abc','xxx',a))                # 'sub'方法匹配规则的前半部分，将符合的字符/字符串替换为规则的后半部分
# print(re.split('-',b))                      # 'split'方法匹配规则字符/字符串对已有的字符/字符串进行分割，返回一个列表
# print(re.split('[-,:]',b))                  # 也可以复杂匹配
#
# obj = re.compile('abc')                     # 'compile'方法将常用的匹配规则定义为类并赋值到一个对象，匹配时用该对象直接匹配即可
# print(obj.findall(a))


# # 关于模块的导入
# import os,sys
# '''添加项目绝对路径到python路径集中'''
# Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(Base_dir)
#
# from jd_test.app import test_add
# '''此时可以随意导入项目目录下所有py文件'''
# print(test_add.add(1,2))
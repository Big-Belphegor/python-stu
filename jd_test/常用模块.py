__author__ = "Alien"
# os模块
import os

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


# sys模块
import sys

# a = sys.argv[1]             # 外部传参函数，默认是连文件名一起以列表形式输出
# if a == 'pull':
#     print('pulling' )
# else:
#     print('Pushing')

print(sys.path)
__author__ = "Alien"
# from urllib.request import urlopen
# import urllib.error                     # URL异常处理
# from bs4 import BeautifulSoup           # 第三方库，Windows/Linux下解压tar包运行python setup.py install即可

# 初识BeautifulSoup
# html = urlopen('https://www.pythonscraping.com/pages/page1.html')
# bs0bj = BeautifulSoup(html.read(),features="html.parser")   # 将HTML转为BeautifulSoup对象
#
# print(bs0bj.h1)     # 获取HTML中<h1></h1>部分数据


# 当不确定URL是否存在时，如下代码：
# try:
#     html = urlopen('http://192.168.181.161/test')
# except urllib.error.URLError as e:
#     print(e)
# else:
#     if html is None:
#         print('URL not found')
#     else:
#         print(html)

# 当不确定HTML中是否包含某个值是，如下代码：
# html = urlopen('https://www.pythonscraping.com/pages/page1.html')
# bs0bj = BeautifulSoup(html.read(), features="html.parser")
#
# try:
#     badContent = bs0bj.nonExisting.anotherTag       # 如果这个值不存在
# except AttributeError as e:                         # 回抛出AttributeError错误
#     print('Tag was not found')                      # 那么就执行该行
# else:                                               # 否则就执行下面代码
#     if badContent == None:
#         print('Tag was not found')
#     else:
#         print(badContent)

# 综合实例(标准获取URL代码)
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    '''检测URL'''

    try:
        '''检查URL是否存在'''
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        '''检测HTML中是否包body.h1值(可选)'''
        bs0bj = BeautifulSoup(html.read(),features="html.parser")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('https://www.cnblogs.com/perl6/p/6517578.html')     # 尝试放入有效/无效的URL
if title == None:
    print('Title could not be found')
else:
    print(title)
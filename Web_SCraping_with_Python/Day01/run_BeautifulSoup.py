__author__ = "Alien"
from urllib.request import urlopen
# 第三方库，Windows/Linux下解压tar包运行python setup.py install即可
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page1.html')
# 将收集到的HTML转为BeautifulSoup对象，并划分为各种等级
bs0bj = BeautifulSoup(html.read(),features="html.parser")

print(bs0bj.h1)     # 获取HTML中<h1></h1>部分数据

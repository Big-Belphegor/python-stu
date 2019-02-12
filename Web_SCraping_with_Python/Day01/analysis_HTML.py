__author__ = "Alien"
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 实例一，通过属相查找标签
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs0bj = BeautifulSoup(html)
# nameList = bs0bj.findAll("span",{"class":"green"})          # 抓取属性值为green的span标签
# testList = bs0bj.findAll(text="the prince")                 # 抓取匹配text指定字符串的内容，并做成列表
# for name in nameList:
#     print(name.get_text())
# print('"The prince" NUM: ',len(testList))

# 实例二，查找子标签及后代标签
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs0bj = BeautifulSoup(html)
#
# for child in bs0bj.find('table',{"id":"giftList"}).children:        # 只查找子标签
#     print(child)
#
# print("\n============================\n")
#
# for child in bs0bj.find('table',{"id":"giftList"}).descendants:     # 查找后代标签
#     print(child)

# 实例三，处理兄弟标签
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs0bj = BeautifulSoup(html)
#
# for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:     # next_siblings作用：跳过第一个匹配的标签
#     print(sibling)
# 注意：previous_siblings定位最后一行但不需抓取的标签，next_sibling和previous_sibling为匹配单个上面两个为多个。

# 实例四，处理父标签
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs0bj = BeautifulSoup(html)
# print(bs0bj.find("img",{"src":"../img/gifts/img6.jpg"})\
#       .parent.previous_sibling.get_text())                          # parent/parents是抓取父标签函数
#
# print(bs0bj.find("span",{"class":"excitingNote"},text="Keep your friends guessing!")\
#       .parent.next_sibling.get_text())
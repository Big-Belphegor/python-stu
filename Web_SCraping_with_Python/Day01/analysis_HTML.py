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
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs0bj = BeautifulSoup(html)

for child in bs0bj.find('table',{"id":"giftList"}).children:        # 只查找子标签
    print(child)

print("\n============================\n")

for child in bs0bj.find('table',{"id":"giftList"}).descendants:     # 查找后代标签
    print(child)

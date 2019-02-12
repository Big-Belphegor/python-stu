__author__ = "Alien"
from urllib.request import urlopen
# 获取URL并打开
html = urlopen('https://www.pythonscraping.com/pages/page1.html')

print(html.read())
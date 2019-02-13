__author__ = "Alien"
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# 实例一，动态爬取网站有用的链接
# html = urlopen('https://segmentfault.com/channel/backend')
# bs0bj = BeautifulSoup(html)
#
# for link in bs0bj.find('footer',{"id":"footer"}).findAll('a',href=re.compile('^http*')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# 实例二，自动在已爬取的链接地址下继续爬取
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('https://segmentfault.com'+articleUrl)
    # html = urlopen(articleUrl)
    bs0bj = BeautifulSoup(html,'html.parser')
    return bs0bj.find('footer',{"id":"footer"}).findAll('a',href=re.compile('^http*'))

links = getLinks('/channel/backend')
while len(links):
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]    # random.randint(a,b)随机函数，取a-b之间任意一个值
    print(newArticle)
    # links = getLinks(newArticle)

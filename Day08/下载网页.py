__author__ = "Alien"
# 基础爬虫，下载整个页面
from urllib import request
from gevent import monkey
import gevent,time

# def uu(url):
#     print('Get: %s' % url)
#     resp = request.urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data),url))
#
# uu('https://www.baidu.com')

# 同步/异步爬虫
monkey.patch_all()      # 把当前所有IO操作做标记

def f(url):
    print('Get: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data),url))


urls = ['https://www.python.org',
        'https://www.yahoo.com',
        'https://www.github.com'
        ]

## 同步部分
time_start = time.time()
for i in urls:
    f(i)
print('同步爬虫费时：',time.time()-time_start)

## 异步部分
async_time_start = time.time()
gevent.joinall(
    [
        gevent.spawn(f,'https://www.python.org'),
        gevent.spawn(f,'https://www.yahoo.com'),
        gevent.spawn(f,'https://www.github.com')
    ]
)
print('异步爬虫费时：',time.time()-async_time_start)
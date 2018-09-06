__author__ = "Alien"
# 在单线程下执行出多线程的感觉
from greenlet import greenlet

def  test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()


# 自动判断IO操作
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)             # 遇到后跳转到下一个方法
    print('Explict context switch to foo again.')

def bar():
    print('Running in bar')
    gevent.sleep(1)             # 再次遇到跳转到上一个方法
    print('Implicit context switch back to bar.')

gevent.joinall(
    [
        gevent.spawn(foo),      # 开始运行
        gevent.spawn(bar)
    ]
)

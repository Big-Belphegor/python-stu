__author__ = "Alien"

# 静态方法
class test(object):
    def __init__(self,x):
        self.x = x
    @staticmethod       # 让其下方的方法不能调用类的self
    def fun1(self):     # 添加该静态方法后将self去掉
        # print('%s is %s' % (self.x,'Teacher'))
        print('%s is %s' % ('Jsion','Teacher'))

# a = test('Jsion')
# a.fun1()

# b = test('xxx')
# b.fun1(b)




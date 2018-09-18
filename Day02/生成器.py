__author__ = "Alien"
# 生成器，看似已经全部生成，其实是逐个生成，只有执行next才会有新的值。
n = 0
s = (x*2 for x in range(10))
while n<10:
    # print(s.__next__())
    print(next(s))              # 等同上面的方法，建议使用该方法
    n +=1
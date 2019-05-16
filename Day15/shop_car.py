__author__ = "Alien"
# 练习
shop_list = [
    ('Mac Book Pro',13000),
    ('Apple Watch',3016),
    ('Iphone XS',12000)
]
#isdigit判断前面变量是否为数值
saveing=input('Input your money,please >')
if saveing.isdigit():
    saveing=int(saveing)
#enumerate能够将列表中数值以索引-值得形式打印，后面的参数1表示让打印的第一个所以从1开始
# for i in enumerate(shop_list,1):
#     print(i)
for x,y in enumerate(shop_list,1):
    print(x,'>',y)
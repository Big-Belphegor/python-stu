__author__ = "Alien"
# 异常处理（对即将出现的错误做出预判，简单说就是将预期内的错误改成自己想要的返回模式）
# 比如：列表a没有第三个索引，当用户查找第三个索引时，不要系统报错，而是自定义的错误提示。
a = [1,2]
try:                            # 尝试执行...
    a[3]

except IndexError as e:         # 除非遇到xxx错误 as xxx，然后执行...
    print('没有这个索引！')
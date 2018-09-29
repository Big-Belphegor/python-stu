__author__ = "Alien"
import re

# 正则符号'.'，只能代指一个字符
r = re.findall('w..l','Hello world')
r2 = re.findall('w.l','Hello world')
print(r)
print(r2)

# 正则符号'^'，匹配开头
s = re.findall('^H','Hello world')
print(s)

# 正则符号'$'，匹配结尾
s = re.findall('d$','Hello world')
print(s)

# 正则符号'*'，匹配任意或0个字符
s = re.findall('a.*d','abcdefg')
s1 = re.findall('a*','abcdefg')
print(s)        # 匹配以a开头d结尾中间不管有多少个字符
print(s1)

# 正则符号'+'，匹配前字符不限制个数
t = re.findall('h+t','hhhhthhhh')
t2 = re.findall('h+','hhhhthhhh')
print(t)
print(t2)

# 正则符号'?'，匹配[]内的字符
a = re.findall('a?c','abcd')
print(a)

# 正则符号'[]'，匹配[]内的字符
a = re.findall('[a,c]','abcd')
print(a)

# 正则符号'{}'，匹配'{}'前面的字符取'{}'内的范围
a = re.findall('a{1,2}b','aaaabcd')
a2 = re.findall('a{1,3}b','aaaabcd')
a3 = re.findall('a{1,3}b','aaaacd')
print(a)
print(a2)
print(a3)
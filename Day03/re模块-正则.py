__author__ = "Alien"
import re
######### 部分一：元字符 #########
# # 正则符号'.'，只能代指一个字符
# r = re.findall('w..l','Hello world')
# r2 = re.findall('w.l','Hello world')
# print(r)
# print(r2)
#
# # 正则符号'^'，匹配开头
# s = re.findall('^H','Hello world')
# print(s)
#
# # 正则符号'$'，匹配结尾
# s = re.findall('d$','Hello world')
# print(s)
#
# # 正则符号'*'，匹配任意或0个字符
# s = re.findall('a.*d','abcdefg')
# s1 = re.findall('a*','abcdefg')
# print(s)        # 匹配以a开头d结尾中间不管有多少个字符
# print(s1)
#
# # 正则符号'+'，匹配前字符不限制个数
# t = re.findall('h+t','hhhhthhhh')
# t2 = re.findall('h+','hhhhthhhh')
# print(t)
# print(t2)
#
# # 正则符号'?'，匹配[]内的字符
# a = re.findall('a?c','abcd')
# print(a)
#
# # 正则符号'[]'，匹配[]内的字符
# a = re.findall('[a,c]','abcd')
# print(a)
#
# # 正则符号'{}'，匹配'{}'前面的字符取'{}'内的范围
# a = re.findall('a{1,2}b','aaaabcd')
# a2 = re.findall('a{1,3}b','aaaabcd')
# a3 = re.findall('a{1,3}b','aaaacd')
# print(a)
# print(a2)
# print(a3)

# # 字符集
# a = re.findall('[cn,com]','www.baidu.com')  # 二选一
# a2 = re.findall('[1-9,a-z,A-Z]','ab12CD')
# a3 = re.findall('[1-9a-zA-Z]','ab12CD')
# a4 = re.findall('[^f]','abcfde')            # 取反
# a5 = re.findall('[^1,2]','1234')            # 取反，两个要是都有就都取反
# print(a)
# print(a2)
# print(a3)
# print(a4)
# print(a5)

# 元字符'\'，作用：将其后面的元字符变为普通字符(就是转义符)，将部分普通字符赋予特殊功能如：\n,\r,\d等
# \d 匹配任何十进制数，相当于[0-9]
# \D 匹配任何非数值字符，相当于[^0-9]
# \s 匹配任何空白字符，相当于[\t\n\r\f\v]
# \S 匹配任何非空白字符，相当于[^\t\n\r\f\v]
# \w 匹配任何字母数字字符，相当于[a-zA-Z0-9]
# \W 匹配任何非字母数字字符，相当于[^a-zA-Z0-9]
# \b 匹配一个字符与特殊字符之间的空隙，这个空隙类似空格
#
# print(re.search('\d{2}','a1234'))
# print(re.findall('\d{2}','a123'))
# print(re.findall(r'a\b','a,/12'))
# print(re.findall(r'/\b','a,/12'))


# 使用search做正则
# a = re.search('\d{2}','a1234')
# print(a.group())
# a2 = re.search('\+','a+b').group()
# print(a2)
# print(re.findall(r'\\','abc\c'))
# print(re.findall(r'\\c','abc\c'))
#
# # 正则符号'()'，将内部的字符串变为一个组
# print(re.findall('(ab)|A','abcd'))
##分组使用
# a = re.search('(?P<n1>a{3})(?P<n2>b{3})','aaabbbccc')       # re.search('(?P<组名>要匹配的内容)(...)','字符串')
# print(a.group())
# print(a.group('n1'))    # 打印n1匹配到的结果
# print(a.group('n2'))    # 打印n2匹配到的结果


######### 部分二：re模块内置方法 #########

# findall：所有结果都返回到一个列表中
# search：返回匹配到的第一个对象以对象的方式返回，可通过group()打印返回结果

# match：只在字符串开始匹配
a = re.match('a','bac')
a2 = re.match('a','abc')
print(a)            # 无法匹配
print(a2.group())   # 匹配到字符'a'与search一样需要使用group获取

# split：分割
a = re.split(':','Name: Lee')               # 用':'分割
a2 = re.split('[:,_]','Name: Alien_Lee')    # 先用':'分割，再用'_'分割剩下的部分
print(a)
print(a2)

# sub：替换匹配内容
a = re.sub('A.*n','Lee','Alien')
print(a)
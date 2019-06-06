__author__ = "Alien"

import re

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def check(x):
    '''检查非合法字符'''
    flag = True
    if re.findall('[a-zA-Z]',x):
        print('Input character error.')
        flag = False

    return flag

def format(x):
    '''格式化字符串'''
    x = x.replace(' ','')
    x = x.replace('++','+')
    x = x.replace('--','-')
    x = x.replace('//','/')
    return x


if check(s):
    source = format(s)


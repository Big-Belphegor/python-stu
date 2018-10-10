__author__ = "Alien"
import time,os

n=0

with open('num_file','r',encoding='utf-8') as f2:
    line=0
    for i in f2.read():
        line+=1
    x = line/2
    print('现在执行次数：',x)

if x<=500:
    # time.sleep(1)
    os.system('reboot')
    n+=1
else:
    print('Over')


with open('num_file','a',encoding='utf-8') as f:
    f.write(str(n)+'\n')



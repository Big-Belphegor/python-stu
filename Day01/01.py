# 读模式，打开文件(只读)
# data = open("Big world",'r')
# a = data.read()
# data.close()
# print(a)

# 写模式，打开文件(创建文件)
# x = open("Write file",'w')
# x.write("Frist time to write. \n")
# x.write("Second time to write.")
# x.close()

# 追加模式，打开文件在文件末尾追加
# b = open("Write file",'a')
# b.write('\nThis oneline is append!')
#
# b.close()

# 最高效文件循环方式
# f = open("Big world",'r')
# n = 0
# for line in f:
#     n += 1
#     if n == 9:
#         print(line.strip())
#         print("This is 9 line")
#         break
#     print(line.strip())

# 文件指针tell 和 seek
# f = open("Big world",'r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# f.seek(0)
# print(f.tell())

# 手动刷新内存数据至硬盘
# data1=open("testfile",'w')
# data1.write("one\n")
# data1.flush()
# 测试，上述理论
# import sys,time
#
# for i in range(50):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.1)

# 截取字符函数，从指针位开始截取任意位
# f = open("Write file",'a')
# f.truncate(10)

# 读写，在光标出追加写入数据
# f = open("Write file",'r+')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.seek(0)
# f.write("123456")

# 创建二进制文件
# f = open("Bfile",'wb')
# f.write("haha".encode())        # 需要转化为二进制
# f.close()

# 文件的修改，将file01中的某个部分修改并存到file02
# f1 = open("File01",'r')
# f2 = open("File02",'w')
# for i in f1:
#     if "This is a replace" in i:
#         i = i.replace("This is a replace","=============")
#     f2.write(i)
#
# f1.close()
# f2.close()

# with... as...:，自动关闭文件
# with open("File01",'r') as f:
#     for i in f:
#         print(i.strip())
#
# with open("File01",'r') as f1,open("File02",'r') as f2:
#     for i in f1:
#         print(i.strip())
#
#     for i in f2:
#         print(i.strip())

# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#
# test(1,z=3,y=2)
# test(1,y=2,z=3)

# 定义多个参数
# def tt(*args):          # 接受位置参数，转换为元组
#     print (args)
#
# tt(1,2,3,4,5,6)
#
# def tt2(**kwargs):      # 接受关键参数，转换为字典
#     print (kwargs)

# 定义全局变量、局部变量
# a = "Lxt"                               # 全局变量
#
# def change_name(a):
#     print ("Before change name :",a)
#     a = "Alien Lee"                     # 局部变量
#     print ("After change name :",a)
#
# print ("全局变量：",a)
# b = change_name(a)

def calc(n):
    print ("-->",n)
    if n>0:
        n = int(n/2)
        return calc(n)
    print ("--->",n)
calc(10)
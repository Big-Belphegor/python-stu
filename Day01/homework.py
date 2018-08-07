__author__ = "Alien"

def find_api():
    x = input("Your find char:")
    with open("accessory1.txt",'r') as f:
        for line in f:
            if x in line:
                print("Find '%s' in accessory1 file. That's line: \n%s" % (x,line))

def write_api():
    x = input("Your write:")
    with open("accessory1.txt",'a+') as f:
        f.write(x)

def change_api():
    x = input("Your want to change:")
    y = input("After Changed:")
    date = ""
    with open("accessory1.txt",'r+') as f:
        for line in f:
            if x in line:
                line = line.replace(x,y)
            date += line
    with open("accessory1.txt",'w') as f:
        f.write(date)

def delete_api():
    x = input("Your want delete line:")
    date = ""
    with open("accessory1.txt",'r+') as f:
        for line in f:
            if x in line:
                line = line.replace(x,'')
            date += line
    with open("accessory1.txt",'w') as f:
        f.write(date)


a = input('''
    1. 查看文件
    2. 修改文件
    3. 追加文件
    4. 删除文件
''')

if a == '1':
    find_api()
elif a == '2':
    change_api()
elif a == '3':
    write_api()
elif a == '4':
    delete_api()
else:
    print('No this option')
__author__ = "Alien"
# a = 'Python '
# b = ' Python'
#
# print(a+'< end')
# print(a.rstrip()+'< end')       # 删除尾部空字符
#
# print('First >'+b)
# print('First >'+b.lstrip())     # 删除首部空字符
#
# c = ['alient','tom']
# c.append('end')
# c.insert(1,'first')
#
# d = ['a','b','c']
# print(d.pop(1))                 # 默认删除列表末尾的值，可以指定索引删除，删除信息可以被再次调用
#
# del c[1]
# c.remove('tom')
#
# print(c)
# print(c[0].title())             # 首字母大写
#
# e = ['v','c','a','b','f']
# e.sort()                        # 永久排序，正向
# # e.sort(reverse=True)            # 永久排序，反向排序
# print(e)
#
# f = ['c','e','d','a']
# print(sorted(f))                # 临时排序

# num = list(range(1,6))
# num2 = list(range(1,10,2))
# print(num)
# print(num2)
#
# print(min(num))
# print(max(num))
# print(sum(num))             # 内置常用统计函数

# print(num[2:4])             # 切片
# print(num[:3])
# print(num[2:])
# print(num[-3:])

# n1 = list(range(1,6))
# n2 = n1[:]                  # 复制列表
# print(n2)

# a = (1,2)                   # 元祖
# print(a[0])

# new1 = {'name':'Alien','age':'24'}    # 字典
# print(new1)
# print(new1['name'])
# del new1['age']
# print(new1)

# new2 = {'A':'123','B':'456','C':'789'}
# for x,y in new2.items():        # 遍历整个字典
#     print('Key:'+ x)
#     print('Value:'+ y)
#
# for x in new2.keys():           # 遍历字典的key
#     print('Key:'+ x)
#
# for y in new2.values():         # 遍历字典的value
#     print('Value:'+ y)

# 字典+列表
# favorite_languages = {
#     'alien':['Python','Shell'],
#     'tom':['C','Go'],
#     'jack':['Java']
# }
#
# for name,languages in favorite_languages.items():
#     print('\n'+ name.title() +' favorite languages is:')
#     for language in languages:
#         print('\t' + language)

# 批量生成“用户”并通过字典赋予信息
# num = []
#
# for x in range(0,10):
#     new_per = {
#         'id':x,
#         'name':'',
#         'age':'',
#         'sex':''
#     }
#     new_per['id'] = x+1
#     num.append(new_per)

# for y in num:
#     print(y)

# while num:
#     users = num.pop()
#     print('Existing users are: ' + str(users))

#============================================================
# for y in num:
#     if y['id'] == 1:
#         message = input('Create ID' + str(y['id']) + ':\n')
#         print(list(message))

# while的其它运用
# unconfirmed_users = ['alien','jack','tom']
# confirmed_users = []
#
# while unconfirmed_users:
#     currnet_user = unconfirmed_users.pop()
#     print('Verifying user:' + currnet_user.title())
#     confirmed_users.append(currnet_user)
#
# print("\nThe following users have been confirmed:")
# for user in confirmed_users:
#     print(user.title())

# def build_person(frist_name,last_name,age=''):
#     person = {'frist':frist_name,'last':last_name,'age':age}
#     return person
#
# musician = build_person('Alien','Lee')
# print(musician)

# def make_pizza(*args):
#     print('\nMaking a pizza with the following toppings:')
#     for top in args:
#         print('- %s' % top)
#
# make_pizza('a','b','c')
# make_pizza('d')

# 类相关示例
# class Dog():                            # 创建类
#     def __init__(self,name,age):        # 创建方法
#         self.name = name                # 定义属性
#         self.age = age
#
#     def sit(self):
#         print('%s is now sitting' % self.name)
#
#     def roll_over(self):
#         print('%s rolled over!' % self.name)
#
# my_dog = Dog('GG',2)                    # 创建实力
# you_dog = Dog('LL',3)
#
# print('My dog name is ' + my_dog.name)  # 调用方法
# print('My dog is ' + str(my_dog.age) + ' years old.')
# print('My dog name is ' + you_dog.name)
# print('My dog is ' + str(you_dog.age) + ' years old.')

# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0               # 设定默认值，此属性不需要再上面特殊定义
#
#     def read_odometer(self):
#         print('This car has ' + str(self.odometer) + ' miles on it')
#
#     def update_odometer(self,mileage):  # 通过方法修改属性
#         self.odometer = mileage
#
#     def other_function(self):
#         pass

# one_car = Car('Audi','R8','2018')
# one_car.read_odometer()
#
# # 修改类中属性的值
# one_car.odometer = 200              # 方法一，通过实例直接访问属性并修改
# one_car.read_odometer()
#
#
# one_car.update_odometer(600)        # 方法二，通过类里的方法修改属性
# one_car.read_odometer()

# # 继承
# class ElectricCar(Car):
#     '''Car的子类，演示继承'''
#
#     def __init__(self,make,model,year):         # 设定与父类完全相同的属性
#         super().__init__(make,model,year)       # 关联父类的所有属性
#         self.battery_size = 70                  # 给子类定义属性
#
#     def describe_battery(self):                 # 定义方法
#         print('This car battery size: %s ' % self.battery_size)
#
# two_car = ElectricCar('Audi','A6','2017')
# two_car.read_odometer()
# two_car.describe_battery()

# 练习
# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print('Restaurant Name: ' + self.restaurant_name + '\nCuisine Type: ' + self.cuisine_type)
#
#     def open_restaurant(self):
#         print('Working...')
#
#     def set_number_served(self,full_numbers):
#         self.number_served = full_numbers
#         return self.number_served
#
#     def increment_nuber_served(self,increase_number):
#         self.number_served += increase_number
#
#
# class User():
#
#     def __init__(self,first_name,last_name,age,sex):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.sex = sex
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print('''
#         Name: %s%s
#         Age: %s
#         Sex: %s
#         ''' % (self.first_name,self.last_name,self.age,self.sex))
#
#     def greet_user(self):
#         print('Welcome %s' % self.first_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         return self.login_attempts
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         return self.login_attempts
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ['Can add post', 'Can delete post', 'Can ban user']
#
#     def show_privileges(self):
#         x = ''
#         for privileges in self.privileges:
#             x += '\t\t\t- ' + privileges + '\n'
#         return x
#
# class Admin(User):
#     def __init__(self,first_name,last_name,age,sex):
#         super().__init__(first_name,last_name,age,sex)
#         self.privileges = Privileges()
#
#     def show_info(self):
#         print('''
#         =========Admin info=========
#         ID: %s %s
#         Message:
#         \t- Age: %s
#         \t- Sex: %s
#         Privileges: \n%s
#         ''' % (self.first_name,self.last_name,self.age,self.sex,str(self.privileges.show_privileges())))

# u1 = User('Alien','Lee','24','m')
# login_attempts = u1.increment_login_attempts()
# print(login_attempts)
# login_attempts = u1.reset_login_attempts()
# print(login_attempts)

# admin = Admin('Alien','Lee','24','M')
# admin.show_info()

# 文件和异常
# file_path = '/etc/nginx/nginx.conf' # 其它目录下文件的导入需要指定绝对路径
# with open(file_path) as nginx:
#     f = nginx
#     print(f)
#
# with open('file.txt') as file:      # 打开file.txt文件，给予别名file. 注意：不指定打开方式时，默认是只读模式'r'
#     '''示例一'''
#     f = file.read()                 # 将file全部导出，赋值给f
#     print(f.rstrip())               # 打印f并去除尾部空行
#     '''示例二'''
#     for line in file:               # 逐行读取
#         print(line.rstrip())
#     '''示例三'''
#     lines = file.readlines()        # 将文件内容以列表的形式全部导出
#     for line in lines:
#         print(line.rstrip())
#     print(type(lines))
#     '''示例四'''
#     lines = file.readlines()        # 使用文件的内容
#     num = ''
#     for line in lines:
#         num += line.strip()         # strip()用于去除空格
#     print(num)

# message = 'I really like dogs'
# print(message.replace('dogs','money'))        # 字符串替换函数

# filename = 'file_two.txt'
# with open(filename,'w') as file:        # 'w'写入文件，如果文件不存在直接创建、文件存在会先清空再写入
#     file.write('============\n')
#     file.write('Hello world!\n')
#     file.write('============')
#
# with open(filename,'a') as file:        # 'a'附加文件，在文件末尾处添加写入的内容，如果文件不存在会直接创建
#     file.write('\n>> END <<\n')
#
# with open(filename,'r+') as file:
#     file.write('test')
#     lines = file.readlines()
#     print(lines)

# try-except-else
# while True:
#     one_num = input("First number:")
#     if one_num == 'q':
#         break
#     two_num = input("Second number:")
#     try:                                        # try下编写可能出现异常的代码部分
#         x = int(one_num) / int(two_num)
#     except ZeroDivisionError:                   # except下指定异常类型，当try部分代码发生异常且与异常类型匹配则运行except下代码
#         print("You cat't divide by zero!")
#     else:                                       # 当try下代码部分没出现任何异常，则执行else下代码
#         print(x)


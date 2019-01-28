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

def build_person(frist_name,last_name,age=''):
    person = {'frist':frist_name,'last':last_name,'age':age}
    return person

musician = build_person('Alien','Lee')
print(musician)
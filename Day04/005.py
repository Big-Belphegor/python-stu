__author__ = "Alien"
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        # 添加学生信息
        self.students.append(stu_obj)
        print("新学员：%s 创建ID" % stu_obj.name)

    def hire(self,staff_obj):
        # 添加老师信息
        self.staffs.append(staff_obj)
        print("新员工：%s 创建ID" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ----- info of Teacher %s -----
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        ''' % (self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ----- info of Student %s -----
        Name: %s
        Age: %s
        Sex: %s
        Stu_id: %s
        Grade: %s
        ''' % (self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tuition for %s." % (self.name,amount))


school = School('菜鸟集团','天堂大街-250')

teacher_001 = Teacher('Jsion',24,'M',15000,'PythonDevOps')
teacher_002 = Teacher('Tom',25,'M',20000,'Linux-system')

student_001 = Student('Alien',19,'M',8001,'PythonDevOps')
student_002 = Student('Hy',19,'F',8002,'Linux-system')


school.hire(teacher_001)
school.hire(teacher_002)
school.enroll(student_001)
school.enroll(student_002)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for i in school.students:
    i.pay_tuition(15000)

# 多态：一个接口多种实现
class Animal(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Miao~")

class Dog(Animal):
    def talk(self):
        print("Wang~")

a = Cat("mm")
b = Dog("gg")

a.talk()
b.talk()

# 多态的实现：
# 方法一
# def all(obj):
#     obj.talk()
#
# all(a)
# all(b)
# 方法二(将上面的函数放到父类里)
Animal.talk(a)
Animal.talk(b)
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



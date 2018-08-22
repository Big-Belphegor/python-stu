__author__ = "Alien"

class School(object):
    # 学校级别
    def __init__(self,addr,course):
        self.addr = addr
        self.course = course
        self.students_Shanghai = []
        self.students_Beijing = []
        self.teachers_Shanghai = []
        self.teachers_Beijing = []

    def hire(self,obj_teacher):
        # 添加老师信息
        if obj_teacher.addr == "上海":
            self.teachers_Shanghai.append(obj_teacher)
        elif obj_teacher.addr == "北京":
            self.teachers_Beijing.append(obj_teacher)

    def enroll(self,obj_student):
        # 添加学生信息
        if obj_student.addr == "上海":
            self.students_Shanghai.append(obj_student)
        elif obj_student.addr == "北京":
            self.students_Beijing.append(obj_student)

class Classpro(School):
    # 班级级别
    def __init__(self,addr,course,classname):
        super(Classpro,self).__init__(addr,course)
        self.classname = classname
        self.class_cost = {"Python":15000,"Linux":11000,"Go":20000}
        self.classnames = []

    def enroll_class(self,obj_class):
        # 添加班级信息
        if obj_class.classname == "Python" and obj_class.addr == "上海":
            self.classnames.append(obj_class)
            # print("您的课程总费用为：%s RMB" % self.class_cost["Python"])
        elif obj_class.classname == "Linux" and obj_class.addr == "上海":
            self.classnames.append(obj_class)
            # print("您的课程总费用为：%s RMB" % self.class_cost["Linux"])
        elif obj_class.classname == "Go" and obj_class.addr == "北京":
            self.classnames.append(obj_class)
            # print("您的课程总费用为：%s RMB" % self.class_cost["Go"])
        else:
            print("您选择的课程还未开班，请耐心等待。")

class Teacher(Classpro):
    # 老师级别
    def __init__(self,addr,classname,course,name,salary,teacher_ID):
        super(Teacher,self).__init__(addr,classname,course)
        self.name = name
        self.salary = salary
        self.teacher_ID = teacher_ID

    def check_myprofile(self):
        # 打印老师相关信息
        print('''
        ----- Info of teacher %s -----
        员工ID： %s
        姓名： %s
        薪资： %s
        课程： %s
        班级： %s
        ''' % (self.name,self.teacher_ID,self.name,self.salary,self.course,self.classname))

    def check_students(self):
        # 打印老师下学生信息
        if self.addr == "上海":
            stu_list = self.students_Shanghai
        else:
            stu_list = self.students_Beijing
        print('''
        ----- Info of stduents -----
        学生名单： %s
        学生人数： %s
        ''' % (stu_list,len(stu_list)))

class Student(Classpro):
    # 学生级别
    def __init__(self,addr,course,classname,student_id,name):
        super(Student,self).__init__(addr,course,classname)
        self.students_id = student_id
        self.name = name

    def check_stuprofile(self):
        # 打印学生相关信息
        print('''
        ----- Info of yourself %s -----
        上课地址： %s
        上课内容： %s
        上课班级： %s
        姓名： %s
        学号： %s
        '''% (self.name,self.addr,self.course,self.classname,self.name,self.students_id))

    def pay(self,obj_pay):
        # 课程学费支付(由于为练习程序，就以打印价格体现)
        if obj_pay.course in self.class_cost:
            print("您需要的学费为：%s" % self.class_cost[obj_pay.course])
        else:
            print("信息错误，请确认后重试！")

# 交互界面
while True:
    num = input('''
    1. 校园界面
    2. 教师界面
    3. 学生界面
    ''')
    if num == '1':
        while True:
            x = input('''
            1. 创建学校
            2. 创建教师
            3. 退出
            ''')
            if x == '1':
                # create school
                check_addr = input('''
                ----- 学校地区选择 ----
                北京
                上海
                ''')
                if check_addr == "北京":
                    check_course = input('''
                    Go
                    ''')
                elif check_addr == "上海":
                    check_course = input('''
                    Python
                    Linux
                    ''')
                else:
                    print("请输入正确信息！")
                s1 = School(check_addr,check_course)

            elif x == '2':
                # create teacher
                teacher_addr = input('办公地址:')
                teacher_classname = input('所属班级:')
                teacher_course = input('教授课程：')
                teacher_name = input('姓名：')
                teacher_salary = input('薪资：')
                teacher_ID = input('员工账号：')
                t1 = Teacher(teacher_addr,teacher_classname,teacher_course,teacher_name,teacher_salary,teacher_ID)
                s1.hire(t1)

            elif x == '3':
                print("Bye!")
                break
            else:
                print("输入信息有误！")
                continue

    elif num == '2':
        while True:
            x = input('''
            1. 查看教师信息
            2. 查看学生信息
            3. 退出
            ''')
            if x == '1':
                t1.check_myprofile()
            elif x == '2':
                t1.check_students()
            elif x == '3':
                print('Bye')
                break
            else:
                print("输入信息有误！")
                continue

    elif num == '3':
        while True:
            x = input('''
            1. 注册
            2. 缴费
            3. 退出
            ''')
            if x == '1':
                # create student
                stu_addr = input('''
                --- 上课地址 ---
                上海
                北京
                ''')
                stu_course = input('''
                --- 选择课程 ---
                Python
                Go
                Linux
                ''')
                stu_classname = input('''
                --- 班级选择 ---
                Python
                Go
                Linux
                ''')
                stu_student_id = input('学号：')
                stu_name = input('姓名：')
                stu1 = Student(stu_addr,stu_course,stu_classname,stu_student_id,stu_name)
                s1.enroll(stu1)

            elif x == '2':
                stu1.pay()
            elif x =='3':
                print('Bye')
                break
            else:
                print('输入信息有误！')
                continue

        else:
            print('输入信息有误！')
            continue

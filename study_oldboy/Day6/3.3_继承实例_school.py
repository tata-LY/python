#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-29 10:29
# @Author  : liuyang
# @File    : 3.3_继承实例_school.py
# @Software: PyCharm

class School(object):
    """初始化学校信息"""
    def __init__(self, name, addr):
        self.name = name
        self.addr =  addr
        self.students = []
        self.staffers = []

    def enroll(self, stu_obj):
        """学生注册"""
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        """聘用老师"""
        print("[%s]学校聘用了老师[%s]。" % (self.name, staff_obj.name))
        self.staffers.append(staff_obj)
        
class SchoolMember(object):
    """初始化学校成员信息"""
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        """打印成员信息"""
        pass

class Teacher(SchoolMember):
    """初始化老师"""
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        """重构父类的tell方法"""
        super(Teacher, self).tell()
        print("""---- info of Teacher:%s -----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        """ % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        """教学"""
        print("%s is teaching course [%s]" % (self.name, self.course))

class Student(SchoolMember):
    """初始化学生"""
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        """重构父类的tell方法"""
        super(Student, self).tell()
        print("""---- info of Student:%s -----
        Name:%s
        Age:%s
        Sex:%s
        Stu_ID:%s
        Grade:%s
        """ % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        """交学费"""
        print("%s has paid tution for $%s" % (self.name, amount))

school1 = School('湖南工业大学', '湖南株洲')
t1 = Teacher("Oldboy", 56, "F", 200000, "Linux")
t2 = Teacher("Alex", 32, "M", 30000, "Python")
s1 = Student('LiuYang', 29, "M", 1001, "Python")
s2 = Student('ZhangJuan', 28, "F", 1002, "Linux")

t1.tell()       # 打印信息
s1.tell()       # 打印信息

school1.hire(t1)        # [湖南工业大学]学校聘用了老师[Oldboy]。
school1.hire(t2)        # [湖南工业大学]学校聘用了老师[Alex]。
school1.enroll(s1)      # 为学员LiuYang办理注册手续
school1.enroll(s2)      # 为学员ZhangJuan办理注册手续

print(school1.students)     # [<__main__.Student object at 0x00000214EB0D8C10>, <__main__.Student object at 0x00000214EB0D8C70>]
print(school1.staffers)     # [<__main__.Teacher object at 0x00000214EB0D8B80>, <__main__.Teacher object at 0x00000214EB0D8BB0>]

school1.staffers[0].teach() # Oldboy is teaching course [Linux]
school1.staffers[0].tell()

for stu in school1.students:
    stu.pay_tuition(5000)
"""
LiuYang has paid tution for $5000
ZhangJuan has paid tution for $5000
"""
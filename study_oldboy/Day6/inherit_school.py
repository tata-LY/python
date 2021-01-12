#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print("[%s]学校为学员[%s]办理注册手续" % (self.name, stu_obj.name))
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("[%s]学校聘用了老师[%s]。" % (self.name, staff_obj.name))
        self.teachers.append(staff_obj)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        # 打印个人信息
        pass

class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""---- info of Teacher:%s -----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        """ % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))

class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print("""---- info of Student:%s -----
        Name:%s
        Age:%s
        Sex:%s
        Stu_ID:%s
        Grade:%s
        """ % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tution for $%s" % (self.name, amount))


school1 = School("湖南工业大学", "湖南株洲")

t1 = Teacher("Oldboy", 56, "F", 200000, "Linux")
t2 = Teacher("Alex", 32, "M", 3000, "PythonDevOps")


s1 = Student('LiuYang', 26, "M", 1001, "PythonDevOps")
s2 = Student('ZhangJuan', 25, "F", 1002, "Linux")

t1.tell()
s1.tell()

school1.hire(t1)
school1.hire(t2)
school1.enroll(s1)
school1.enroll(s2)

print(school1.students)
print(school1.teachers)

school1.teachers[0].teach()

for stu in school1.students:
    stu.pay_tuition(5000)
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
import os
import json

class People(object):
    """学校成员类"""
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(People):
    """老师类"""
    def __init__(self, name, age, sex, salary, class_name):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.class_name = class_name
        self.data = {           # 字典数据方便已json方式存储到数据库file里
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'salary': self.salary,
            'class': self.class_name,
        }

class Teacher_manage(object):
    """老师管理类"""
    def get_teacher(self, name):
        """获取老师信息，返回字典数据"""
        data_operate = DataOperate('teacher')
        return data_operate.select(name)

    def mod_teacher(self, name, age, sex, salary, class_name):
        """修改老师信息，返回bool值"""
        teacher = Teacher(name, age, sex, salary, class_name)
        data_operate = DataOperate('teacher')
        return data_operate.update(teacher)


class Student(People):
    """学生类"""
    def __init__(self, name, age, sex, class_name):
        super(Student, self).__init__(name, age, sex)
        self.class_name = class_name
        self.data = {       # 字典数据方便已json方式存储到数据库file里
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'class': self.class_name,
        }

class Student_manage(object):
    """学生管理类"""
    def __init__(self):
        school = School()
        self.classes = school.view_class()  # 学校班级数据，列表格式

    def student_registry(self, name, age, sex, class_name):
        """学生注册，return bool"""
        student = Student(name, age, sex, class_name)
        data_operate = DataOperate('student')
        return data_operate.add(student)

    def student_payment(self, course_name):
        """学生交学费，return 课程价格"""
        data_operate = DataOperate('course')
        course_dict = data_operate.select(course_name)
        return course_dict['price']

    def get_student(self, name):
        """获取学生信息，return dict"""
        data_operate = DataOperate('student')
        return data_operate.select(name)

class Classes(object):
    """班级类"""
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.data = {
            'name': self.name,
            'course': self.course
        }

class Course(object):
    """课程类"""
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price
        self.data = {
            'name': self.name,
            'period': self.period,
            'price': self.price,
        }

class School(object):
    """学校类，主要是学校进行一些初始化操作"""
    def __init__(self):
        self.courses = []
        self.classes = []
        self.teachers = []

    def create_course(self, name, period, price):
        """创建课程，return bool"""
        course = Course(name, period, price)    # 实例化课程类
        data_operate = DataOperate('course')    # DataOperate数据操作实例化
        return data_operate.add(course)         # 返回True/False

    def view_course(self):
        """查看课程，return list"""
        data_operate = DataOperate('course')
        self.courses = data_operate.select_all()    # select_all 获取所有数据
        return self.courses

    def create_class(self, name, course_name):
        """创建班级，return bool"""
        c = Classes(name, course_name)
        data_operate = DataOperate('class')
        return data_operate.add(c)

    def view_class(self):
        """查看班级，return list"""
        data_operate = DataOperate('class')
        self.classes = data_operate.select_all()    # select_all 获取所有数据
        return self.classes

    def create_teacher(self, name, age, sex, salary, class_name):
        """聘用老师，return bool"""
        teacher = Teacher(name, age, sex, salary, class_name)
        data_operate = DataOperate('teacher')
        return data_operate.add(teacher)

    def view_teacher(self):
        """查看老师，return list"""
        data_operate = DataOperate('teacher')
        self.teacher = data_operate.select_all()    # select_all 获取所有数据
        return self.teacher

class DataOperate(object):
    """数据库操作类，增删改查"""
    def __init__(self, data_table):
        self.data_table = data_table    # 数据库表=file名
        self.data_dir = os.path.join(settings.BASE_DIR, settings.DATABASE['path'], settings.DATA_TABLE[data_table])     # 拼接数据文件的路径路径

    def select(self, name):
        """获取data_dir下文件名为name的字典数据并返回"""
        data = {}
        data_file = os.path.join(self.data_dir, name)
        if os.path.exists(data_file):
            with open(data_file, "r", encoding="utf-8") as f_r:
                data = json.loads(f_r.read())
        return data

    def select_all(self):
        """获取data_dir下所有数据并返回一个列表数据，列表元素为每个数据文件内的字典数据"""
        data = []
        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                data_file = os.path.join(root, file)
                with open(data_file, "r", encoding="utf-8") as f_r:
                    data.append(json.loads(f_r.read()))
        return data

    def add (self, obj):
        """将字典数据obj.data写入到data_dir下obj.name名下"""
        data_file = os.path.join(self.data_dir, obj.name)
        if os.path.exists(data_file):
            return False    # 文件存在返回False
        else:
            with open(data_file, "w", encoding="utf-8") as f_w:
                f_w.write(json.dumps(obj.data))
            return True

    def update (self, obj):
        """这里的update跟add差不多，覆盖地将obj.data数据写入到已经存在的data_dir/obj.name文件"""
        data_file = os.path.join(self.data_dir, obj.name)
        if os.path.exists(data_file):
            with open(data_file, "w", encoding="utf-8") as f_w:
                f_w.write(json.dumps(obj.data))
            return True
        else:
            return False    # 文件不存在返回False

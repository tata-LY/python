#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
import os
import json

class People(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(People):
    def __init__(self, name, age, sex, salary, class_name):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.class_name = class_name
        self.data = {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'salary': self.salary,
            'class': self.class_name,
        }

class Teacher_manage(object):
    def get_teacher(self, name):
        data_operate = DataOperate('teacher')
        return data_operate.select(name)

    def mod_teacher(self, name, age, sex, salary, class_name):
        teacher = Teacher(name, age, sex, salary, class_name)
        data_operate = DataOperate('teacher')
        return data_operate.update(teacher)


class Student(People):
    def __init__(self, name, age, sex, class_name):
        super(Student, self).__init__(name, age, sex)
        self.class_name = class_name
        self.data = {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'class': self.class_name,
        }

class Student_manage(object):
    def __init__(self):
        school = School()
        self.classes = school.view_class()

    def student_registry(self, name, age, sex, class_name):
        student = Student(name, age, sex, class_name)
        data_operate = DataOperate('student')
        return data_operate.add(student)

    def student_payment(self, course_name):
        data_operate = DataOperate('course')
        course_dict = data_operate.select(course_name)
        return course_dict['price']

    def get_student(self, name):
        data_operate = DataOperate('student')
        return data_operate.select(name)

class Classes(object):
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.data = {
            'name': self.name,
            'course': self.course
        }

class Course(object):
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
    def __init__(self):
        self.courses = []
        self.classes = []
        self.teachers = []

    def create_course(self, name, period, price):
        course = Course(name, period, price)
        data_operate = DataOperate('course')
        return data_operate.add(course)

    def view_course(self):
        data_operate = DataOperate('course')
        self.courses = data_operate.select_all()
        return self.courses

    def create_class(self, name, course_name):
        c = Classes(name, course_name)
        data_operate = DataOperate('class')
        return data_operate.add(c)

    def view_class(self):
        data_operate = DataOperate('class')
        self.classes = data_operate.select_all()
        return self.classes

    def create_teacher(self, name, age, sex, salary, class_name):
        teacher = Teacher(name, age, sex, salary, class_name)
        data_operate = DataOperate('teacher')
        return data_operate.add(teacher)

    def view_teacher(self):
        data_operate = DataOperate('teacher')
        self.teacher = data_operate.select_all()
        return self.teacher

class DataOperate(object):
    def __init__(self, data_table):
        self.data_table = data_table
        self.data_dir = os.path.join(settings.BASE_DIR, settings.DATABASE['path'], settings.DATA_TABLE[data_table])

    def select(self, name):
        data = {}
        data_file = os.path.join(self.data_dir, name)
        if os.path.exists(data_file):
            with open(data_file, "r", encoding="utf-8") as f_r:
                data = json.loads(f_r.read())
        return data

    def select_all(self):
        data = []
        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                data_file = os.path.join(root, file)
                with open(data_file, "r", encoding="utf-8") as f_r:
                    data.append(json.loads(f_r.read()))
        return data

    def add (self, obj):
        data_file = os.path.join(self.data_dir, obj.name)
        if os.path.exists(data_file):
            return False
        else:
            with open(data_file, "w", encoding="utf-8") as f_w:
                f_w.write(json.dumps(obj.data))
            return True

    def update (self, obj):
        data_file = os.path.join(self.data_dir, obj.name)
        if os.path.exists(data_file):
            with open(data_file, "w", encoding="utf-8") as f_w:
                f_w.write(json.dumps(obj.data))
            return True
        else:
            return False

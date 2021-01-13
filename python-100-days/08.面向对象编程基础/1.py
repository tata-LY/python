#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-12 16:08
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

class Student(object):

    def __init__(self, name, age):
        """
        __init__是一个特殊方法用于在创建对象时进行初始化操作
        :param name: 初始化学生名字
        :param age: 初始化学生年龄
        """
        self.name = name
        self.age = age

    def study(self, course_name = 'Python'):
        print('%s正在学习%s.' % (self.name, course_name))

    def display_stu_info(self):
        print('%s: %s岁' % (self.name, self.age))


def main():
    stu1 = Student('刘洋', 29)
    stu1.study('Golang')
    stu1.display_stu_info()

    stu2 = Student('肥肥仔', 28)
    stu2.study('Math')
    stu2.display_stu_info()
if __name__ == '__main__':
    main()
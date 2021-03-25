#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-23 10:23
# @Author  : liuyang
# @File    : main.py
# @Software: PyCharm

from core import teacher_view, student_view

def run():
    info = """
    [1] 老师视图
    [2] 学生视图
    [q] 退出
    """
    while True:
        print("欢迎来到LYZJ学员管理系统".center(30, "*"))
        print(info)
        choice = input(">>>").strip()
        if choice == '1':
            teacher_view.TeacherView()
        elif choice == '2':
            student_view.StudentView()
        elif choice in ['q', 'Q']:
            exit('Goodbye')
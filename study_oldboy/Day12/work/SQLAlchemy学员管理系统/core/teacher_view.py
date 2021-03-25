#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-23 14:06
# @Author  : liuyang
# @File    : teacher_view.py
# @Software: PyCharm

from database import table_class
from core import common

class TeacherView(object):
    def __init__(self):
        self.interactive()

    def auth(self):
        """选择老师视图时登录验证"""
        print("老师视图登录".center(30, "*"))
        name = input("用户名>>>").strip()
        password = input("密码>>>").strip()
        self.teacher_data = table_class.session.query(table_class.Teacher).filter(table_class.Teacher.name==name, table_class.Teacher.password==password).first()

    def display_classes(self):
        print("[%s]老师授课班级显示".center(30, "#") % self.teacher_data.name)
        print("ID\t班级名\t课程")
        for classes in self.teacher_data.classes:
            print("%d\t%s\t%s" % (classes.id, classes.classes_name, classes.course))
        input("")

    def add_classes(self):
        print("添加班级".center(30, "#"))
        while True:
            classes_name = input("班级名>>>").strip()
            if table_class.session.query(table_class.Classes).filter(table_class.Classes.classes_name==classes_name).first():
                print("班级已存在，请重新输入！")
            else:
                break
        course = input("课程名>>>").strip()
        classes_obj = table_class.Classes(classes_name=classes_name, course=course)
        # 添加授课老师
        teachers = table_class.session.query(table_class.Teacher).all()
        classes_obj.teacher = []
        for teacher in teachers:
            choice = input("是否添加[%s]老师为授课老师[Y/N]>>>" % teacher.name).strip()
            if choice in ['y', 'Y', 'yes', 'YES']:classes_obj.teacher.append(teacher)
        table_class.session.add(classes_obj)
        table_class.session.commit()

    def add_student(self):
        print("添加学员".center(30, "#"))
        while True:
            name = input("学员name>>>").strip()
            if table_class.session.query(table_class.Student).filter(table_class.Student.name==name).first():
                print("学员已存在，请重新输入！")
            else:
                break
        password = input("登录密码>>>").strip()
        while True:
            qq = input("学员QQ>>>").strip()
            if common.qq_isok(qq):
                if table_class.session.query(table_class.Student).filter(table_class.Student.qq == qq).first():
                    print("学员QQ已存在，请重新输入！")
                else:
                    break
            else:
                print("输入的QQ号不合法！")
        student_obj = table_class.Student(name=name, password=password, qq=qq)
        # 添加班级
        classes = table_class.session.query(table_class.Classes).all()
        student_obj.classes = []
        for cla in classes:
            choice = input("该学员是否报名了[%s %s]课程[Y/N]>>>" % (cla.classes_name, cla.course)).strip()
            if choice in ['y', 'Y', 'yes', 'YES']:student_obj.classes.append(cla)
        table_class.session.add(student_obj)
        table_class.session.commit()

    def add_course_record(self):
        print("添加课程上课记录".center(30, "#"))
        teach_classes = self.teacher_data.classes
        classes_dict = {}
        for cla in teach_classes:
            print(cla.course)
            classes_dict[cla.course] = cla
        choice = input("选择添加的课程>>>").strip()
        if choice in classes_dict:
            choice_classes = classes_dict[choice]
            while True:
                print("所有上课记录".center(30, "-"))
                for course_record in choice_classes.course_record:
                    print(course_record.name)
                choice = input("是否添加上课记录[Y/N]").strip()
                if choice in ['y', 'Y', 'yes', 'YES']:
                    name = 'Day' + str(len(choice_classes.course_record)+1)
                    classes_id = choice_classes.id
                    classes_course = table_class.CourseRecord(name=name, classes_id=classes_id)
                    classes_course.student=[]

                    for stu in choice_classes.student:
                        classes_course.student.append(stu)
                    table_class.session.add(classes_course)
                    table_class.session.commit()
                else:
                    break
        else:
            print("您输入的课程不存在")


    def modify_study_record(self):
        print("修改学员课程成绩".center(30, "#"))
        for teach_class in self.teacher_data.classes:
            print("修改[%s]班[%s]科目成绩".center(30, "-") % (teach_class.classes_name, teach_class.course))
            for student in teach_class.student:
                for course_record in teach_class.course_record:
                    study_record = table_class.session.query(table_class.StudyRecord).filter(table_class.StudyRecord.student_id==student.id, table_class.StudyRecord.course_record_id==course_record.id, table_class.StudyRecord.status=='Y', table_class.StudyRecord.score==None).first()
                    if study_record:
                        while True:
                            score = input("学生[%s][%s %s]课程分数[0-100]>>>" % (student.name, teach_class.course, course_record.name)).strip()
                            if common.score_isok(score):
                                score = int(score)
                                break
                            else:
                                print("输入的分数不合法")
                        study_record.score = score
                        table_class.session.commit()
            else:
                print("所有作业都已经批改")

    def view_homework_ranking(self):
        while True:
            print("查看成绩排名".center(30, "#"))
            all_classes = {}
            for classes in self.teacher_data.classes:
                print(classes.classes_name, classes.course)
                all_classes[classes.classes_name] = classes
            choice_classes = input("选择班级,exit退出>>>")
            if choice_classes in all_classes:
                data = table_class.session.query(table_class.Student.name, table_class.func.sum(table_class.StudyRecord.score)).filter(table_class.StudyRecord.course_record_id==table_class.CourseRecord.id, table_class.CourseRecord.classes_id==all_classes[choice_classes].id, table_class.StudyRecord.student_id==table_class.Student.id).group_by(table_class.StudyRecord.student_id).order_by(table_class.func.sum(table_class.StudyRecord.score).desc()).all()
                for item in data:
                    print(item)
            elif choice_classes == 'exit':break
            else:
                print("错误的选项！")

    def interactive(self):
        self.auth()
        if self.teacher_data:
            choice_dict = {
                '1': ['显示班级', self.display_classes],
                '2': ['添加班级', self.add_classes],
                '3': ['添加学员', self.add_student],
                '4': ['添加课程上课记录', self.add_course_record],
                '5': ['修改学员课程成绩', self.modify_study_record],
                '6': ['查看成绩排名', self.view_homework_ranking],
                'b': ['返回'],
                'q': ['退出'],
            }
            while True:
                print("老师视图".center(30, "*"))
                for key in choice_dict:
                    print("[%s] %s" % (key, choice_dict[key][0]))
                choice = input(">>>").strip()
                if choice in ['b', 'B']:break
                elif choice in ['q', 'Q', 'exit']:exit("Goodbye")
                elif choice in choice_dict:choice_dict[choice][1]()
                else:
                    print("错误的选项！")

        else:
            print("用户或者密码错误！")

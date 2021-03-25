#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-23 14:06
# @Author  : liuyang
# @File    : StudentView.py
# @Software: PyCharm

from database import table_class

class StudentView(object):
    def __init__(self):
        self.interactive()

    def auth(self):
        """选择学生视图时登录验证"""
        print("学生视图登录".center(30, "*"))
        name = input("用户名>>>").strip()
        password = input("密码>>>").strip()
        self.student_data = table_class.session.query(table_class.Student).filter(table_class.Student.name==name, table_class.Student.password==password).first()

    def upload_homework(self):
        print("所有作业信息".center(30, "#"))
        # 作业情况展示
        # for study_record in table_class.session.query(table_class.StudyRecord).filter(table_class.StudyRecord.student_id==self.student_data.id).all():
        #     course_record = table_class.session.query(table_class.CourseRecord).filter(table_class.CourseRecord.id==study_record.course_record_id).first()
        #     if study_record.status == 'Y':
        #         print("%s %s 已提交作业" % (course_record.classes.course, course_record.name))
        #     else:
        #         print("%s %s 未提交作业" % (course_record.classes.course, course_record.name))

        # print("开始上传作业".center(30, "-"))
        # for study_record in table_class.session.query(table_class.StudyRecord).filter(
        #     table_class.StudyRecord.student_id == self.student_data.id, table_class.StudyRecord.status==None).all():
        #     course_record = table_class.session.query(table_class.CourseRecord).filter(table_class.CourseRecord.id==study_record.course_record_id).first()
        #     choice = input("是否提交[%s]课程[%s]的作业[Y/N]>>>" % (course_record.classes.course, course_record.name)).strip()
        #     if choice in ['y', 'Y', 'yes', 'YES']:
        #         study_record.status = 'Y'
        #         table_class.session.commit()

        # 作业情况展示（联合查询）
        data = table_class.session.query(table_class.StudyRecord.id, table_class.Classes.course, table_class.CourseRecord.name, table_class.StudyRecord.status).filter(table_class.StudyRecord.student_id==self.student_data.id, table_class.StudyRecord.course_record_id==table_class.CourseRecord.id, table_class.CourseRecord.classes_id==table_class.Classes.id).all()
        for item in data:
            if item[3] == 'Y':
                print("%s %s 已提交作业" % (item[1], item[2]))
            else:
                print("%s %s 未提交作业" % (item[1], item[2]))
        print("开始上传作业".center(30, "-"))

        for item in data:
            if item[3] != 'Y':
                choice = input("是否提交[%s]课程[%s]的作业[Y/N]>>>" % (item[1], item[2])).strip()
                if choice in ['y', 'Y', 'yes', 'YES']:
                    study_record = table_class.session.query(table_class.StudyRecord).filter(table_class.StudyRecord.id==item[0]).first()
                    study_record.status = 'Y'
                    table_class.session.commit()


    def view_homework_results(self):
        while True:
            print("查看作业成绩".center(30, "#"))
            all_classes = {}
            for classes in self.student_data.classes:
                print(classes.course)
                all_classes[classes.course] = classes
            choice_classes = input("选择查看成绩的课程,exit退出>>>")
            if choice_classes in all_classes:
                for course_record in all_classes[choice_classes].course_record:
                    for study_record in table_class.session.query(table_class.StudyRecord).filter(table_class.StudyRecord.student_id==self.student_data.id, table_class.StudyRecord.course_record_id==course_record.id, table_class.StudyRecord.status=='Y'):
                        print(choice_classes, course_record.name, study_record.score)
            elif choice_classes == 'exit':
                break
            else:
                print("错误的选项！")

    # def view_homework_ranking(self):
    #     print("view_homework_ranking")

    def interactive(self):
        self.auth()
        if self.student_data:
            choice_dict = {
                '1': ['上传作业', self.upload_homework],
                '2': ['查看作业成绩', self.view_homework_results],
                # '3': ['查看成绩排名', self.view_homework_ranking],
                'b': ['返回'],
                'q': ['退出']
            }
            while True:
                print("学生视图".center(30, "*"))
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
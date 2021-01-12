#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from core import all_class
from core import logger

def student_registry():
    print("学生注册：")
    name = input("名字>>>")
    age = input("年龄>>>")
    sex = input("性别>>>")
    class_name = ''
    s_manage = all_class.Student_manage()
    flag = True
    while flag:
        print("当前所有班级：")
        for key, item in enumerate(s_manage.classes):
            print(key, item)
        choice = input("输入选择的班级编号>>>")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(s_manage.classes):
                class_name = s_manage.classes[choice]['name']
                course_name = s_manage.classes[choice]['course']
                flag = False
            else:
                print("Invalid option !")
        else:
            print("Invalid option !")
    if s_manage.student_registry(name, age, sex, class_name):
        print("学生[%s]注册成功！" % name)
        print("班级课程[%s]需要缴费$%s" % (course_name, s_manage.student_payment(course_name)))
        logger.logger('course', "学生[%s]注册成功！" % name)
    else:
        print("注册失败，学生[%s]已经注册过！" % name)
        logger.logger('course', "注册失败，学生[%s]已经注册过！" % name)
    input("输入任意键继续：")

def student_view():
    name = input("输入查看的学生名字：")
    s_manage = all_class.Student_manage()
    student_dict = s_manage.get_student(name)
    if student_dict:
       print("学生信息：\n%s" % student_dict)
    else:
        print("输入的学生名字不存在！")
    input("输入任意键继续：")

def student_mod():
    name = input("输入需要修改的学生名字：")
    s_manage = all_class.Student_manage()
    student_dict = s_manage.get_student(name)
    if student_dict:
       print("学生信息：\n%s" % student_dict)
    else:
        print("输入的学生名字不存在！")
    input("暂时不修改，输入任意键继续：")

def teacher_look_course():
    name = input("输入查看的老师名字：")
    t_manage = all_class.Teacher_manage()
    teacher_dict = t_manage.get_teacher(name)
    if teacher_dict:
       print("老师信息：\n%s" % teacher_dict)
    else:
        print("输入的老师名字不存在！")
    input("输入任意键继续：")

def teacher_view():
    name = input("输入查看的老师名字：")
    t_manage = all_class.Teacher_manage()
    teacher_dict = t_manage.get_teacher(name)
    if teacher_dict:
       print("老师信息：\n%s" % teacher_dict)
    else:
        print("输入的老师名字不存在！")
    input("输入任意键继续：")

def teacher_mod():
    name = input("输入查看的老师名字：")
    t_manage = all_class.Teacher_manage()
    teacher_dict = t_manage.get_teacher(name)
    name = teacher_dict['name']
    age = teacher_dict['age']
    sex = teacher_dict['sex']
    class_name = teacher_dict['class']
    if teacher_dict:
        print("老师信息：\n%s" % teacher_dict)
        salary = input("老师[%s]新的薪水>>>" % teacher_dict['name'])
        if t_manage.mod_teacher(name, age, sex, salary, class_name):
            print("修改老师[%s]信息成功！" % name)
            logger.logger('course', "修改老师[%s]信息成功！" % name)
        else:
            print("修改老师[%s]失败！" % name)
            logger.logger('course', "修改老师[%s]失败！" % name)
    else:
        print("输入的老师名字不存在！")
    input("输入任意键继续：")
def school_create_course():
    print("创建课程：")
    name = input("课程名>>>")
    period = input("周期>>>")
    price = input("价格>>>")
    school = all_class.School()
    if school.create_course(name, period, price):
        print("创建课程[%s]成功！" % name)
        logger.logger('course', "创建课程[%s]成功！" % name)
    else:
        print("创建失败，课程[%s]已经存在！" % name)
        logger.logger('course', "创建失败，课程[%s]已经存在！" % name)
    input("输入任意键继续：")


def school_create_class():
    print("创建班级：")
    name = input("班级名>>>")
    school = all_class.School()
    course_list = school.view_course()
    course_name = ''
    flag = True
    while flag:
        print("当前所有开设的课程：")
        for key, item in enumerate(course_list):
            print(key, item)
        choice = input("输入选择的课程编号>>>")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(course_list):
                course_name = course_list[choice]['name']
                flag = False
            else:
                print("Invalid option !")
        else:
            print("Invalid option !")
    if school.create_class(name, course_name):
        print("创建班级[%s]成功！" % name)
        logger.logger('course', "创建班级[%s]成功！" % name)
    else:
        print("创建失败，班级[%s]已经存在！" % name)
        logger.logger('course', "创建失败，班级[%s]已经存在！" % name)
    input("输入任意键继续：")

def school_add_teacher():
    print("添加老师：")
    name = input("老师名字>>>")
    age = input("年龄>>>")
    sex = input("性别>>>")
    salary = input("薪水>>>")
    school = all_class.School()
    class_list = school.view_class()
    class_name = ''
    flag = True
    while flag:
        print("当前所有班级：")
        for key, item in enumerate(class_list):
            print(key, item)
        choice = input("输入选择的班级编号>>>")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(class_list):
                class_name = class_list[choice]['name']
                flag = False
            else:
                print("Invalid option !")
        else:
            print("Invalid option !")
    if school.create_teacher(name, age, sex, salary, class_name):
        print("添加老师[%s]成功！" % name)
        logger.logger('course', "添加老师[%s]成功！" % name)
    else:
        print("添加失败，老师[%s]已经存在！" % name)
        logger.logger('course', "添加失败，老师[%s]已经存在！" % name)
    input("输入任意键继续：")

def school_view_course():
    school = all_class.School()
    course_list = school.view_course()
    print("课程信息如下：")
    for course  in course_list:
        print(course)
    input("输入任意键继续：")

def school_view_class():
    school = all_class.School()
    class_list = school.view_class()
    print("班级信息如下：")
    for c  in class_list:
        print(c)
    input("输入任意键继续：")
def school_view_teacher():
    school = all_class.School()
    teacher_list = school.view_teacher()
    print("老师信息如下：")
    for teacher  in teacher_list:
        print(teacher)
    input("输入任意键继续：")
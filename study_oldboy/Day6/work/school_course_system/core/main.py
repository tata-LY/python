#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys
from core import auth
from core.auth import login_required
from core.operate import *

is_auth = True

@login_required
def student_interactive(*args):
   while True:
      menu = u'''
      \033[32;1m学生视图:
      1.学生注册
      2.查看个人信息
      3.修改个人信息
      4.[b]返回上一层
      5.[q]退出系统\033[0m'''
      menu_dic = {
          '1': student_registry,
          '2': student_view,
          '3': student_mod,
      }
      print(menu)
      choice = input("请选择>>>")
      if choice in menu_dic:
         menu_dic[choice]()
      elif choice == "b":
         break
      elif choice == "q":
         logout()
      else:
         print("Invalid option !")

@login_required
def teacher_interactive(*args):
   while True:
      menu = u'''
      \033[32;1m老师视图:
      1.查看授课信息
      2.查看个人信息
      3.修改个人信息
      4.[b]返回上一层
      5.[q]退出系统\033[0m'''
      menu_dic = {
          '1': teacher_look_course,
          '2': teacher_view,
          '3': teacher_mod,
      }
      print(menu)
      choice = input("请选择>>>")
      if choice in menu_dic:
         menu_dic[choice]()
      elif choice == "b":
         break
      elif choice == "q":
         logout()
      else:
         print("Invalid option !")

@login_required
def school_interactive(*args):
   while True:
      menu = u'''
      \033[32;1m学校视图:
      1.创建课程
      2.创建班级
      3.添加老师
      4.查看课程信息
      5.查看班级信息
      6.查看老师信息
      7.[b]返回上一层
      8.[q]退出系统\033[0m'''
      menu_dic = {
         '1': school_create_course,
         '2': school_create_class,
         '3': school_add_teacher,
         '4': school_view_course,
         '5': school_view_class,
         '6': school_view_teacher,
      }
      print(menu)
      choice = input("请选择>>>")
      if choice in menu_dic:
         menu_dic[choice]()
      elif choice == "b":
         break
      elif choice == "q":
         logout()
      else:
         print("Invalid option !")

def logout(*args):
   exit("Goodbye!")

def run():
   while True:
      menu = u'''
      \033[32;1m欢迎来到湖南工业大学选课系统:
      1.学生视图
      2.老师视图
      3.学校视图
      4.[q]退出系统\033[0m'''
      menu_dic = {
          '1': student_interactive,
          '2': teacher_interactive,
          '3': school_interactive,
      }
      print(menu)
      choice = input("请选择>>>")
      if choice in menu_dic:
         is_auth = auth.account_login(choice)
         if is_auth:
            menu_dic[choice](is_auth)
         else:
            print("输入的口令不正确 !" )
      elif choice == "q":
         logout()
      else:
         print("Invalid option !")
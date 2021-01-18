#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 8:48
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm


_user ="alex"
_passwd = "abc123"
counter = 0
while counter <3:
    username = input("Username:")
    password = input("Password:")
    if username == _user and password == _passwd :
        print("Welcome %s login...." % _user)
        break #跳出，中断
    else:
        print("Invalid username or password !")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还想玩么?[y/n]")
        if keep_going_choice == "y":
            counter = 0

else:
    print("要不要脸，臭流氓啊，小虎。")

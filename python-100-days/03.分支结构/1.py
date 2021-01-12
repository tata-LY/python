#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 10:08
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

# if 用户身份验证
username = input("用户名：")
password = input("密码：")
if username == "admin" and password == "123456":
    print("用户%s登录成功！" % username)
else:
    print("用户或者密码错误！")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 14:27
# @Author  : liuyang
# @File    : 7_decorater.py
# @Software: PyCharm


user, passwd = 'liuyang', '123456'
def auth(func):
    def wrapper(*args, **kwargs):
        username = input("Username>>>").strip()
        password = input("Password>>>").strip()

        if user == username and passwd == password:
            print("\033[32;1mUser har passed authentication!\033[0m")
            func(*args, **kwargs)
        else:
            print("\033[31;1mInvalid username or password!\033[0m")
    return wrapper


@auth
def index():
    print('welcome to index page')
@auth
def home():
    print('welcome to home page')
    return 'from home'
@auth
def bbs():
    print('welcome to bbs page')

index()
print(home())  # return的结果是None
bbs()
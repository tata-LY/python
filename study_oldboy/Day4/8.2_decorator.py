#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 14:51
# @Author  : liuyang
# @File    : 8.2_decorator.py
# @Software: PyCharm

user, passwd = 'liuyang', '123456'

def auth(auth_type):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if auth_type == 'local':
                username = input("Username>>>").strip()
                password = input("Password>>>").strip()

                if user == username and passwd == password:
                    print("\033[32;1mUser har passed authentication!\033[0m")
                    result = func(*args, **kwargs)
                    print(result)
                    return result # 保持被装饰的函数的return
                else:
                    print("\033[31;1mInvalid username or password!\033[0m")
            elif auth_type == 'ladp':
                print("\033[32;1mNo ladp!\033[0m")
            else:
                print("\033[31;1mWrong authentication method!\033[0m")

        return inner_wrapper # 这里如果写成return inner_wrapper(), 不需要调用就直接执行了。
    return outer_wrapper


@auth(auth_type='xxxx')
def index():
    print('welcome to index page')

@auth(auth_type='local')
def home():
    print('welcome to home page')
    return 'from home'

@auth(auth_type='ladp')
def bbs():
    print('welcome to bbs page')
    return 'from bbs'

index()
home()
bbs()
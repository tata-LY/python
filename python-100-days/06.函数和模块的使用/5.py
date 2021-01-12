#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-6 13:51
# @Author  : liuyang
# @File    : 5.py
# @Software: PyCharm
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


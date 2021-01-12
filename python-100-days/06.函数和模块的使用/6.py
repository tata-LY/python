#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-6 13:54
# @Author  : liuyang
# @File    : 6.py
# @Software: PyCharm

"""全局变量a不会被修改"""
def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100


"""全局变量a被修改"""
def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
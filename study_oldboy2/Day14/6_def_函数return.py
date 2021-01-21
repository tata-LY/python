#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 14:59
# @Author  : liuyang
# @File    : 6_def_函数return.py
# @Software: PyCharm

def test1():
    pass

def test2():
    return 0

def test3():
    return 0,'hello',['a','b','c'],{'name':'alex'}

def test4():
    return test2

x=test1()
y=test2()
z=test3()
a = test4()

print(x)
print(y)  # 单个返回值
print(z)  # 过个值时以元组方式返回
print(a)    # 返回一个函数
print(a())  # 放回的函数可以再调用
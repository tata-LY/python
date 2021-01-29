#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-29 10:18
# @Author  : liuyang
# @File    : 3.2_多继承顺序.py
# @Software: PyCharm

class A():
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        print("B")

class B2(A):
    pass

class C(A):
    def __init__(self):
        print("C")

class D1(B1, C):
    pass

class D2(B2, C):
    pass

d1 = D1()       # B
d2 = D2()       # C

"""
python3 上经典类和新式类都是按广度优先来继承的。
python2 经典类按深度优先来继承的，新式类按广度优先继承的。
"""
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

class A():
    def __init__(self):
        print("A")


class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    # python3 上经典类和新式类都是按广度优先来继承的。
    # python2 经典类按深度优先来继承的，新式类按广度优先继承的。
    pass

d1 = D()
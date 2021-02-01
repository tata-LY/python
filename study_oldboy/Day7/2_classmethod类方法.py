#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 9:54
# @Author  : liuyang
# @File    : 2.classmethod类方法.py
# @Software: PyCharm

class Dog(object):
    n = 'TATA'        # 调用类变量可以成功
    def __init__(self, name):
        self.name = name
        # self.n = 'Tata'       # 不成功

    @ classmethod       # 只能访问类变量，不能访问实例变量
    def eat(self):
        print("%s is eating %s" % (self.n, '包子'))

    def talk(self):
        print('%s is talking' % self.name)

d = Dog("ZhangJuan")
d.eat()     # TATA is eating 包子

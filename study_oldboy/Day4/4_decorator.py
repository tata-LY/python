#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 13:34
# @Author  : liuyang
# @File    : 4_decorater.py
# @Software: PyCharm

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()

foo()


x = 0
def granpa():
    x = 1
    def father():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    father()
granpa()
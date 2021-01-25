#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 11:04
# @Author  : liuyang
# @File    : 2_decorater.py
# @Software: PyCharm

def foo():
    print('in the foo')

def bar(func):
    func()
    print('in the bar')

bar(foo)
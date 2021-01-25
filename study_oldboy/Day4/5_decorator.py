#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 13:43
# @Author  : liuyang
# @File    : 5_decorater.py
# @Software: PyCharm

import time

def test1():
    print('in the test1')
    time.sleep(2)
def test2():
    print('in the test2')
    time.sleep(2)

# 高阶函数
def deco1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' % (stop_time-start_time))
# 没改变源代码、增加了新功能，但是改变了调用方式
deco1(test1)
deco1(test2)

def deco2(func):
    start_time = time.time()
    return func
    stop_time = time.time()
    print('the func run time is %s' % (stop_time-start_time))
# 没改变源代码，没改变调用方式，但是没有新增新的功能。
test1 = deco2(test1)
test2 = deco2(test2)
test1()
test2()

def timmer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time-start_time))
    return deco
# 没改变源代码，没改变调用方式，新增了新的功能
test1 = timmer(test1)
test2 = timmer(test2)
test1()
test2()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 13:59
# @Author  : liuyang
# @File    : 6_decorater.py
# @Software: PyCharm
import time

# 装饰器
def timmer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        print(args, kwargs)
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time-start_time))
    return deco

@timmer
def test1():
    print('in the test1')
    time.sleep(2)

@timmer  # test2 = timmer(test2) = deco  , test2() = deco()
def test2(name, age):
    print('in the test2')
    print('name:%s age:%d' % (name, age))
    time.sleep(2)

@timmer
def test3(name, age, gender):
    print('in the test3')
    print('name:%s age:%d gender:%s' % (name, age, gender))
    time.sleep(2)

test1()
test2('Liuyang', 29)
test3('Zhangjuan', 28, gender='F')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 13:19
# @Author  : liuyang
# @File    : 1_decorater.py
# @Software: PyCharm
import time

def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time-start_time))
    return warpper

@timmer
def test1():
    print('start run func test1')
    time.sleep(3)
    print('in the func test1')

test1()
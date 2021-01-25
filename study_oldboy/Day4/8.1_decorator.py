#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 14:48
# @Author  : liuyang
# @File    : 8.1_decorator.py
# @Software: PyCharm

import time

def deco(def_name):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func()
            stop_time = time.time()
            print("the func %s run time is %s " % (def_name, (stop_time-start_time)))

        return wrapper
    return out_wrapper

@deco(def_name="test1")
def test1():
    print("in the test1")
    time.sleep(3)

@deco(def_name="test2")
def test2():
    print("in the test2")
    time.sleep(2)

test1()
test2()


#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang
import time

def deco(def_name):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func()
            stop_time = time.time()
            print("the func {func_name} run time is {time} ".format(func_name=def_name,time=stop_time - start_time))

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

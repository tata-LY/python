#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 装饰器
import time

def timmer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        print(args,kwargs)
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time - start_time))
    return deco

@timmer
def test1():
    time.sleep(3)
    print("in the test1")
@timmer
def test2(name, age):
    time.sleep(3)
    print("test2: ", name, age)

# test1 = timmer(test1)
test1()
test2("LiuYang", 22)
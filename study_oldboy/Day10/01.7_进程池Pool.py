#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 14:24
# @Author  : liuyang
# @File    : 01.7_进程池Pool.py
# @Software: PyCharm

from multiprocessing import Process, Pool, freeze_support
import time, os

def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i+100

def Bar(arg):
    print("-->exec done:", arg, os.getpid())

if __name__ == '__main__':
    freeze_support()        # 在win上必须这么写
    pool = Pool(processes=3)    # processes=5允许进程池同时放入5个进程
    print("主进程pid：", os.getpid())
    foo_ret = []
    for i in range(10):
        # foo_ret.append(pool.apply_async(func=Foo, args=(i, )))  # 并行
        foo_ret.append(pool.apply_async(func=Foo, args=(i, ), callback=Bar))      # callback=回调,主进程回调。
        # foo_ret.append(pool.apply(func=Foo, args=(i, )))  # 串行

    print('end')
    pool.close()
    pool.join() # 进程池中进程执行完毕后再关闭，如果注释，那么程序不等线程就直接关闭了。
    print(foo_ret)        # 串行执行结果[100, 101, 102, 103, 104]
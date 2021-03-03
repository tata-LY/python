#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-1 14:01
# @Author  : liuyang
# @File    : 01.1_多进程.py
# @Software: PyCharm
"""进程直接调用方式"""


import multiprocessing
import time
import threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print("hello %s" % name)
    t = threading.Thread(target=thread_run, )
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=("liuyang%s" % i, ))
        p.start()
        # p.join()
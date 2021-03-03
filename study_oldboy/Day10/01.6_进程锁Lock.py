#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 14:15
# @Author  : liuyang
# @File    : 01.5_多进程锁lock.py
# @Software: PyCharm
"""进程锁，在屏幕打印的过程中可以保证打印不会乱"""

from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        p = Process(target=f, args=(lock, num))
        p.start()
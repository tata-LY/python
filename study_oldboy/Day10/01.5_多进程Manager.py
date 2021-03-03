#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 9:38
# @Author  : liuyang
# @File    : 01.5_多进程Manager.py
# @Software: PyCharm

"""
可以支持 list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array，并在多个进程间共享和传递，也可以一起修改。
"""

from multiprocessing import Process, Manager
import os

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid())
    print(d)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()      # 生成一个字典，可以在多个进程间共享和传递，可以修改。
        l = manager.list(range(5))      # 生成一个列表，可以在多个进程间共享和传递，可以修改。
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)

        for p in p_list:
            p.join()

        print(d)        # {1: '1', '2': 2, 0.25: None}
        print(l)        # [0, 1, 2, 3, 4, 19640, 17676, 19292, 21156, 20400, 15472, 23540, 18440, 24376, 3984]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 14:45
# @Author  : liuyang
# @File    : 02.7_threading_ex7_lock.py
# @Software: PyCharm

import time
import threading

def run(n):
    global m
    lock.acquire()
    m += 1
    print("n:%s m:%s" % (n, m))
    time.sleep(1)
    lock.release()


if __name__ == '__main__':
    m = 0
    t_objs = []
    lock = threading.Lock()
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))     # 生成一个线程实例
        t.start()
        t_objs.append(t)

    for t in t_objs:
        t.join()

    print(m)


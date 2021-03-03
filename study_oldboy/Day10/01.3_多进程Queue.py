#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-1 15:44
# @Author  : liuyang
# @File    : 01.3_多进程Queue.py
# @Software: PyCharm

"""
父进程的Queue传给子进程时，只能用进程Q（multiprocessing.Queue），不能用线程Q（queue.Queue）
进程Q相当于是克隆
线程Q是操作同一份数据
"""

from multiprocessing import Process, Queue

# from queue import Queue       # 使用线程Q时报错：TypeError: cannot pickle '_thread.lock' object

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())      # [42, None, 'hello']
    p.join()
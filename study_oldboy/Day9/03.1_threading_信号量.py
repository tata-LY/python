#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 15:32
# @Author  : liuyang
# @File    : 03.1_threading_信号量.py
# @Software: PyCharm
"""信号量，同一时间只允许n个线程运行"""

import threading, time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)       # 最多允许5个线程同时运行
    for i in range(1, 21):
        t  = threading.Thread(target=run, args=(i, ))
        t.start()

# while threading.active_count() != 1:
#     pass #print threading.active_count()
# else:
#     print('----all threads done---')
#     print(num)
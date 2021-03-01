#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 16:59
# @Author  : liuyang
# @File    : 05.1_queue队列.py
# @Software: PyCharm

"""
class queue.Queue(maxsize=0) #先入先出 创建一个队列对象（队列容量），若maxsize小于或者等于0，队列大小没有限制
class queue.LifoQueue(maxsize=0) #last in fisrt out
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
"""

import queue
Q = queue.Queue()

print(Q)        # <queue.Queue object at 0x0000022033A60DF0>
print(type(Q))  # <class 'queue.Queue'>

for i in range(5):
    Q.put(i)

#1.基本方法
print(Q.queue)  #查看队列中所有元素      # deque([0, 1, 2, 3, 4])
print(Q.qsize())    #返回队列的大小     # 5
print(Q.empty())    #判断队空           # False
print(Q.full())     #判断队满           # False

while not Q.empty():    # 不空就一直取
    print(Q.get())


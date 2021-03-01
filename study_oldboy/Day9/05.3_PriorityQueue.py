#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 13:22
# @Author  : liuyang
# @File    : 05.3_PriorityQueue.py
# @Software: PyCharm

"""
class queue.Queue(maxsize=0) #先入先出 创建一个队列对象（队列容量），若maxsize小于或者等于0，队列大小没有限制
class queue.LifoQueue(maxsize=0) # 先进后出
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
"""

import queue

q = queue.PriorityQueue()

q.put((5, 'liuyang'))
q.put((3, 'zhangjuan'))
q.put((1, 'liuzhangyi'))
q.put((7, 'liuzhangyiyi'))

print(q.queue)      # [(1, 'liuzhangyi'), (5, 'liuyang'), (3, 'zhangjuan'), (7, 'liuzhangyiyi')]
print(q.qsize())    # 4
print(q.empty())    # False
print(q.full())     # False


while not q.empty():
    print(q.get())

"""
(1, 'liuzhangyi')
(3, 'zhangjuan')
(5, 'liuyang')
(7, 'liuzhangyiyi')
"""
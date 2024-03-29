#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 9:04
# @Author  : liuyang
# @File    : 02.3_redis_pipeline.py
# @Software: PyCharm

"""
redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。
"""
import redis
import time

hostname = '192.168.113.11'
port = 6379
pool = redis.ConnectionPool(host=hostname, port=port, db=1)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('name', 'Liuyang')
time.sleep(10)
pipe.set('age', 29)

pipe.execute()

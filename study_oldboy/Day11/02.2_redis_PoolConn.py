#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-9 10:16
# @Author  : liuyang
# @File    : 02.1.redis_PoolConn.py
# @Software: PyCharm

"""
连接池
redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
"""

import redis
hostname = '192.168.113.11'
port = 6379

pool = redis.ConnectionPool(host=hostname, port=port)
r = redis.Redis(connection_pool=pool)

r.set('foo', 'Bar')
print(r.get('foo'))
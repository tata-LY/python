#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-9 10:10
# @Author  : liuyang
# @File    : 02.1.redis_conn.py
# @Software: PyCharm

"""
操作模式
redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py
"""

import redis
hostname = '192.168.113.11'
port = 6379

r = redis.Redis(host=hostname, port=port)

r.set('foo', 'Bar')
print(r.get('foo'))
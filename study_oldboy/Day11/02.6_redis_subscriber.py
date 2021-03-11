#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 9:47
# @Author  : liuyang
# @File    : 02.6_redis_subscriber.py
# @Software: PyCharm

from RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
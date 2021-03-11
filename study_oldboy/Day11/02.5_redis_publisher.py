#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 9:44
# @Author  : liuyang
# @File    : 02.5_redis_publisher.py
# @Software: PyCharm

from RedisHelper import RedisHelper

obj = RedisHelper()
obj.public('hello')

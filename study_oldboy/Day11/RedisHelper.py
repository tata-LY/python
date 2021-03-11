#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 9:38
# @Author  : liuyang
# @File    : 02.4_redis_helper.py
# @Software: PyCharm

import redis

hostname = '192.168.113.11'
port = 6379

class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host=hostname, port=port)
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_sub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()      # 打开收音机
        pub.subscribe(self.chan_sub)    # 调频道
        pub.parse_response()    # 准备接收
        return pub
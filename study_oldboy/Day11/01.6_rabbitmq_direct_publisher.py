#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 15:11
# @Author  : liuyang
# @File    : 01.py
# @Software: PyCharm
"""
direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
"""
import pika
import sys

hostname = '192.168.113.11'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'INFO'     # 日志级别，默认INFO
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 14:19
# @Author  : liuyang
# @File    : 01.4_rabbitmq_fanout_publisher.py
# @Software: PyCharm

"""
之前的例子都基本都是1对1的消息发送和接收，即消息只能发送到指定的queue里，但有些时候你想让你的消息被所有的Queue收到，类似广播的效果，这时候就要用到exchange了，

An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.

Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息

fanout: 所有bind到此exchange的queue都可以接收消息
direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
"""

import pika
import sys

hostname = '192.168.113.11'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
channel = connection.channel()  # 声明一个管道

# pika版本不同导致的用法不同，解决方法为把type换成exchange_type
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [X] Sent %r" % message)
connection.close()
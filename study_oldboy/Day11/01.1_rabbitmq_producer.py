#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 10:30
# @Author  : liuyang
# @File    : 01.1_rabbitmq_producer.py
# @Software: PyCharm
"""基本用例"""

import pika

hostname = '192.168.113.11'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))

channel = connection.channel()  # 声明一个管道

# 声明queue
# channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello', durable=True)  # durable 队列名持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  #  routing_key 队列名字
                      body='Hello World!',  # body 队列内容
                      properties=pika.BasicProperties(
                          delivery_mode=2,      # 队列数据持久化
                      )
                      )

print(" [x] Sent 'Hello World!'")
connection.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 14:32
# @Author  : liuyang
# @File    : 01.5_rabbitmq_fanout_subscriber.py
# @Software: PyCharm
import pika

hostname = '192.168.113.11'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

"""
TypeError: queue_declare() missing 1 required positional argument: 'queue'
原因：生成了随机的channle,但bug要求我指定channle
解决：''，就是填个空值
"""
result = channel.queue_declare('', exclusive=True)  # exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue
print("random queue_name: ", queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(queue_name,
                      callback,
                      False)

channel.start_consuming()
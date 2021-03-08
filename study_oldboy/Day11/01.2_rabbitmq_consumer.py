#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 10:39
# @Author  : liuyang
# @File    : 01.2_rabbitmq_consumer.py
# @Software: PyCharm

import pika
import time

hostname = '192.168.113.11'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))

# 声明一个管道
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello', durable=True)      # 服务端加了durable队列持久化True

"""
ch：channel管道内存地址
method：
properties：<BasicProperties(['delivery_mode=2'])>
"""
def callback(ch, method, properties, body):
    # print(ch)           # <BlockingChannel impl=<Channel number=1 OPEN conn=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x0000023719057B80> params=<ConnectionParameters host=192.168.113.11 port=5672 virtual_host=/ ssl=False>>>>
    # print(method)       # <Basic.Deliver(['consumer_tag=ctag1.f9c99de711b6433b99292c4077f056df', 'delivery_tag=1', 'exchange=', 'redelivered=False', 'routing_key=hello'])>
    # print(properties)   # <BasicProperties(['delivery_mode=2'])>
    # time.sleep(10)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)      # consumer端确认，完成后删除服务端队列消息数据


# channel.basic_qos(prefetch_count=1)     # 设置QOS，处理完才处理下一个消息
channel.basic_consume(       # 消费消息
                      'hello',    # 队列名字
                      callback,     # 如果收到消息，就调用CALLBACK函数来处理消息
                      # False # 消费者发送确认消息,True不确认，False确认，默认False
                     )

# channel.basic_consume('hello',callback, True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

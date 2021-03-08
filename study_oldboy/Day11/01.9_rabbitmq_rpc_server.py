#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 16:34
# @Author  : liuyang
# @File    : 01.9_rabbitmq_rpc_server.py
# @Software: PyCharm

import pika
import time

hostname = '192.168.113.11'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, properties, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,   # 客户端发过来的随机Q name
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),     # 服务端收到消息调用回调函数取得客户端发过来的uuid再发到客户端进行确认
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume('rpc_queue',
                      on_request        # 接收消息回调
                      )

print(" [x] Awaiting RPC requests")
channel.start_consuming()
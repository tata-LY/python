#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 16:09
# @Author  : liuyang
# @File    : 01.8_rabbitmq_rpc_client.py
# @Software: PyCharm

import pika
import uuid
import time

class FibonacciRpcClient(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.hostname))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare('', exclusive=True)
        self.callback_queue = result.method.queue   # 随机Q，reply_to到服务端
        self.channel.basic_consume(self.callback_queue, # queue name
                                   self.on_response,    # 只要已收到消息就调用on_response
                                   True)

    def on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())    # 随机uuid
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to = self.callback_queue,
                                       correlation_id=self.corr_id  # 发送到服务端，等服务端收到消息后再确认返回到该客户端
                                       ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()   # 非阻塞版的start_consuming()
            print("no message...")
            time.sleep(1)
        return int(self.response)


hostname = '192.168.113.11'
fibonacci_rpc = FibonacciRpcClient(hostname)

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)
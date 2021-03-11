#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-9 8:47
# @Author  : liuyang
# @File    : 01.11_rabbitmq_topic_subscriber.py
# @Software: PyCharm

import pika
import sys

hostname = '192.168.113.11'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [X] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue_name,
                      callback,
                      True)

channel.start_consuming()
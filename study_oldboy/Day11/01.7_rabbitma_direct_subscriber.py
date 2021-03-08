#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-8 15:17
# @Author  : liuyang
# @File    : 01.7_rabbitma_direct_subscriber.py
# @Software: PyCharm

import pika
import sys

hostname = '192.168.113.11'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# severities = sys.argv[1:]
severities = ['INFO', 'WARN', 'ERROR']
if not severities:
    sys.stderr.write("Usage: %s [INFO] [WARN] [ERROR]\n" % sys.argv[0])
    sys.exit(1)

for serverity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=serverity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue_name,
                      callback,
                      False)

channel.start_consuming()

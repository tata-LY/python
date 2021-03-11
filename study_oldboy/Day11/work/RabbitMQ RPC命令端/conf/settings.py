#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 15:18
# @Author  : liuyang
# @File    : settings.py
# @Software: PyCharm

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# rabbitMQ IP
RABBITMQ_IP = '192.168.113.11'
# RabbitMQ 端口
RABBITMQ_PORT = 5672
# 数据持久化True/Fasle
DB_DURABLE = True
# 数据持久化文件
DB_NAME = '%s/db/task_data' % BASE_DIR
# rpc routing_key
QUEUE_NAME = 'rpc_queue'
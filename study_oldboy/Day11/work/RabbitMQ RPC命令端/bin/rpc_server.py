#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 15:21
# @Author  : liuyang
# @File    : rpc_server.py
# @Software: PyCharm

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
import pika
import subprocess
import chardet

class RpcServer(object):
    def __init__(self, IP, PORT, QUEUE_NAME):
        self.IP = IP
        self.PORT = PORT
        self.QUEUE_NAME = QUEUE_NAME
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.IP, port=self.PORT))
        self.channel = self.connection.channel()

    def on_response(self):
        """等待client发过来的QUEUE_NAME并调用call"""
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_qos(prefetch_count=1)    # QOS,处理完这个消息后才接收下一个
        self.channel.basic_consume(self.QUEUE_NAME,
                                   self.call        # 接收消息后回调call函数
                                  )
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def call(self, ch, method, properties, body):
        """接收到client的cmd，将系统cmd结果发送到rabbitMQ"""
        cmd = body.decode()     # 接收到body是二进制格式，例如b'ipconfig'
        print("执行命令：%s" % cmd)
        cmd_response = self.cmd_result(cmd)     # 获取系统cmd执行结果
        ch.basic_publish(exchange='',
                         routing_key=properties.reply_to,  # client发过来的随机callback_queue名，然后server作为routing_key把结果发给client
                         properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                         # 服务端收到消息调用回调函数取得客户端发过来的uuid再发到客户端进行确认
                         body=cmd_response)
        ch.basic_ack(delivery_tag=method.delivery_tag)      # consumer端确认，完成后删除队列消息数据,删除client发过来的cmd命令消息

    def cmd_result(self, cmd):
        """系统执行cmd，并返回cmd结果"""
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        out = res.stdout.readlines()
        err = res.stderr.readlines()
        cmd_result_b = out if out else err      # list格式
        cmd_result = b''
        for line in cmd_result_b:       # 命令结果list转成二进制str
            cmd_result += line
        # print(cmd_result)
        encoding = chardet.detect(cmd_result)['encoding']       # 获取二进制str格式的字符编码
        # print(encoding)
        return cmd_result.decode(encoding)

if __name__ == '__main__':
    IP = settings.RABBITMQ_IP
    PORT = settings.RABBITMQ_PORT
    QUEUE_NAME = settings.QUEUE_NAME
    rpc_server = RpcServer(IP, PORT, QUEUE_NAME)
    rpc_server.on_response()

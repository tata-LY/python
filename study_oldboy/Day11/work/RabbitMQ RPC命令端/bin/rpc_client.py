#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-10 15:21
# @Author  : liuyang
# @File    : rpc_client.py
# @Software: PyCharm

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import pika
import uuid
import json

class RpcClient(object):
    def __init__(self, IP, PORT, QUEUE_NAME):
        self.task_data = self.task_data_init()
        self.IP = IP
        self.PORT = PORT
        self.QUEUE_NAME = QUEUE_NAME
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.IP, port=self.PORT))
        self.channel = self.connection.channel()    # 申明管道
        result = self.channel.queue_declare('', exclusive=True)     # 申明队列
        self.callback_queue = result.method.queue  # 随机Q，reply_to到服务端
        self.channel.basic_consume(self.callback_queue,  # 等待服务端发过来的callback_queue名字
                                   self.on_response,  # 只要收到server端系统执行cmd结果返回消息就调用on_response
                                   True)

    def on_response(self, ch, method, properties, body):
        """接收回调函数，将server系统cmd结果放入task_data字典"""
        if properties.correlation_id in self.task_data:
            self.task_data[properties.correlation_id] = body.decode()   # 接收到body是二进制格式

    def call(self, cmd):
        """将client cmd命令发给RabbitMQ，让server端接收"""
        self.corr_id = str(uuid.uuid4())    # 随机uuid作为task id
        self.task_data[self.corr_id] = None
        self.channel.basic_publish(exchange='',
                                   routing_key=self.QUEUE_NAME,
                                   properties=pika.BasicProperties(
                                       reply_to = self.callback_queue,  # properties.reply_to发给服务端，让服务端作为routing_key发回来
                                       correlation_id=self.corr_id  # 发送到服务端，等服务端收到消息后再确认返回到该客户端
                                       ),
                                   body=cmd)
        while self.task_data[self.corr_id] is None:     # 任务没结果前就一直consuming接收
            self.connection.process_data_events()   # 非阻塞版的start_consuming()接收
        else:
            print("Task id [%s]" % self.corr_id)

    def help(self):
        help_info = """Usage：
        1.输入运行的命令
        2.check_all
        3.check_task [ID]"""
        print(help_info)

    def check_all(self):
        """查看所有的task id"""
        if len(self.task_data) > 0:
            for task_id in self.task_data:
                print(task_id)
        else:
            print("No task")

    def check_task(self, cmd):
        """获取任务执行的结果"""
        cmd_list = cmd.split()
        flag = True
        if len(cmd_list) == 2:
            task_id = cmd_list[1]
            if task_id in self.task_data:
                print(self.task_data[task_id])
                del self.task_data[task_id]
            else:
                flag = False
        else:
            flag = False

        if not flag:
            print("请输入正确的task id")

    def exit(self):
        db_file = settings.DB_NAME
        if settings.DB_DURABLE:
            with open(db_file, 'w', encoding='utf-8') as f_w:
                f_w.write(json.dumps(self.task_data))
        exit('Goodbye')

    def task_data_init(self):
        """
        程序执行，先对任务数据进行初始化。
        """
        task_data = {}
        db_file = settings.DB_NAME
        if settings.DB_DURABLE:
            if os.path.exists(db_file):
                with open(db_file, 'r', encoding='utf-8') as f_r:
                    task_data = json.loads(f_r.read())
            return task_data

    def interactive(self):
        while True:
            # print(self.task_data)
            cmd_str = input(">>> ").strip()
            if len(cmd_str) == 0:continue
            if cmd_str in ['help', 'h', '?']:
                self.help()
            elif cmd_str == 'check_all':
                self.check_all()
            elif cmd_str.split()[0] == 'check_task':
                self.check_task(cmd_str)
            elif cmd_str == 'exit':
                self.exit()
            else:
                self.call(cmd_str)

if __name__ == '__main__':
    IP = settings.RABBITMQ_IP
    PORT = settings.RABBITMQ_PORT
    QUEUE_NAME = settings.QUEUE_NAME
    rpc_client = RpcClient(IP, PORT, QUEUE_NAME)
    rpc_client.interactive()
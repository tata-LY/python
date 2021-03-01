#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 15:22
# @Author  : liuyang
# @File    : core.py
# @Software: PyCharm

from conf import settings
from core.all_class import SshThread, SftThread
import os

def exec_cmd(choice_group):
    while True:
        cmd = input("CMD>>>").strip()
        if cmd == 'exit':break
        t_objs = []
        for host in choice_group:
            ip = host['ip']
            port = host['port']
            username = host['username']
            password = host['password']
            t = SshThread(ip, port, username, password, cmd)
            t.start()
            t_objs.append(t)

        for t in t_objs:
            t.join()

def send_file(choice_group):
    while True:
        send_file = input("SEND FILE>>>").strip()
        if send_file == 'exit':break
        if os.path.exists(send_file) and os.path.isfile(send_file):
            t_objs = []
            for host in choice_group:
                ip = host['ip']
                port = host['port']
                username = host['username']
                password = host['password']
                t = SftThread(ip, port, username, password, send_file)
                t.start()
                t_objs.append(t)
            for t in t_objs:
                t.join()
        else:
            print('输入的SEND FILE不合法')

def group_interactive(group_name, choice_group=[]):
    handle = {
        '1': "exec cmd",
        '2': "send file",
        'b': "返回",
        "q": "退出"
    }
    while True:
        print("[%s]组主机如下：" % group_name)
        for item in choice_group:
            print("\t%s" % item['ip'])
        for index in handle:
            print("%s %s" % (index, handle[index]))
        choice = input("选择>>>")
        if choice == 'b':
            break
        elif choice == 'q':
            exit('Goodbye.')
        elif choice == '1':
            exec_cmd(choice_group)
        elif choice == '2':
            send_file(choice_group)
        else:
            print("输入不合法,请重新选择")


def run():
    hosts = settings.hosts      # 列表
    while True:
        for group in hosts:
            print("%-10s[%s]" % (group, len(hosts[group])))
        choice = input("主机组选择，[q/Q]退出>>>").strip()
        if choice in ['q', 'Q']:
            exit('Goodbye.')
        elif choice in hosts:
            group_name = choice
            choice_group = hosts[choice]
            group_interactive(group_name, choice_group)
        else:
            print("输入不合法,请重新选择")
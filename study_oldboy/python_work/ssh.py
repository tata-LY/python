#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-4 15:39
# @Author  : liuyang
# @File    : ssh.py
# @Software: PyCharm

import paramiko

print("SSH".center(50, '*'))
hostname = input("Hostname>>> ").strip()
port = 22
username = input("Username>>> ").strip()
password = input("Password>>> ").strip()

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname=hostname, port=port, username=username, password=password)

cmd = ''
while cmd not in ['q', 'exit', 'quit', 'b']:
    cmd = input("[%s@%s ~]# " % (username, hostname)).strip()
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)

    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    cmd_result = res if res else err
    print(cmd_result.decode(), end='')

# 关闭连接
ssh.close()

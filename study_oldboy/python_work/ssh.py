#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-4 15:39
# @Author  : liuyang
# @File    : ssh.py
# @Software: PyCharm

import paramiko

print("SSH".center(50, '*'))
ip = input("IP>>> ").strip()
port = 22
username = input("Username>>> ").strip()
password = input("Password>>> ").strip()
session_timeout = 60

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if client.connect(ip, username=username, password=password, timeout=session_timeout):
    print("SSH %s 成功" % ip)
    while True:
        cmd = input("CMD>>> ").strip()
        stdin, stdout, stderr = client.exec_command(cmd)
        for line in stdout:
            print(line, end="")
else:
    print("登录失败")

client.close()
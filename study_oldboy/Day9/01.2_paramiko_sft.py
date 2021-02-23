#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-23 10:54
# @Author  : liuyang
# @File    : 01.2_paramiko_sft.py
# @Software: PyCharm

import paramiko

hostname = '10.5.3.11'
port = 22
username = 'root'
password = 'Liuyang@2021'

transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# 将本地README文件拷贝到远程主机/tmp/README_TEST
sftp.put('README', '/tmp/README_TEST')
# 将远程主机/tmp/test.txt拷贝到本地test.txt
sftp.get('/tmp/test.txt', 'test.txt')

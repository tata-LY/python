#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-23 10:54
# @Author  : liuyang
# @File    : 01.2_paramiko_sft.py
# @Software: PyCharm

import paramiko

hostname = '192.168.113.11'
port = 22
username = 'root'
ssh_rsa_file = 'id_rsa'
private_key = paramiko.RSAKey.from_private_key_file(ssh_rsa_file)

transport = paramiko.Transport((hostname, port))
transport.connect(username=username, pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)

# 将本地README文件拷贝到远程主机/tmp/README_TEST
sftp.put('README', '/tmp/README_TEST')
# 将远程主机/tmp/test.txt拷贝到本地test.txt
sftp.get('/tmp/test.txt', 'test.txt')

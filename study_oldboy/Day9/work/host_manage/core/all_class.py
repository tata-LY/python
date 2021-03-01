#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 16:27
# @Author  : liuyang
# @File    : all_class.py
# @Software: PyCharm

import threading
import paramiko
import os

class SshThread(threading.Thread):
    def __init__(self, ip, port, username, password, cmd):
        super(SshThread, self).__init__()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def run(self):
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(self.cmd)
        # 获取命令结果
        res, err = stdout.read(), stderr.read()
        cmd_result = res if res else err
        # print("%s".center(50, '-') % self.ip)
        print("%s".center(50, '-') % self.ip, "\n", cmd_result.decode(), end='')


class SftThread(threading.Thread):
    def __init__(self, ip, port, username, password, local_file):
        super(SftThread, self).__init__()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.local_file = local_file
        self.remote_file = '/tmp/' + os.path.basename(local_file)       # 上传的文件都存放到/tmp,Linux路径'/'

    def run(self):
        transport = paramiko.Transport((self.ip, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # 将文件拷贝到远程主机/tmp
        sftp.put(self.local_file, self.remote_file)
        print("send[%s]文件到[%s]主机完成" % (self.local_file, self.ip))
# -*- coding: utf-8 -*-
# @Time    : 2021-2-23 14:04
# @Author  : liuyang
# @File    : 01.3_paramiko_ssh_rsa.py
# @Software: PyCharm

import paramiko

hostname = '192.168.113.11'
port = 22
username = 'root'
ssh_rsa_file = 'id_rsa'
# private_key = paramiko.RSAKey.from_private_key_file(ssh_rsa_file)

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname=hostname, port=port, username=username, key_filename=ssh_rsa_file)

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
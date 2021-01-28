#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:30
# @Author  : liuyang
# @File    : 13.3_module_configparser.py
# @Software: PyCharm

""""
python configparser增删改查语法

[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = admin
password = admin

[topsecret.server.com]
host_port = 50022
forwardx11 = no
"""

import configparser
import os

config_file = "13_configparser1.conf"
new_config_file = '13_configparser2.conf'
config = configparser.ConfigParser()

if os.path.exists(config_file):
    config.read(config_file)    # 读取config_file的内容
    config.remove_section('bitbucket.org')  # 删除[bitbucket.org]所有配置
    config.write(open(new_config_file, 'w'))    # 将删除后的数据写入new_config_file

    print(config.has_section('nginx'))  # 判断section是否有nginx    False
    config.add_section('nginx') # 增加nginx section
    config.write(open(new_config_file, 'w'))

    config['nginx']['IP'] = "172.25.2.7"
    config['nginx']['PORT'] = "80"
    config['nginx']['version'] = "1.9.1"
    config['nginx']['info'] = "test"
    config.write(open(new_config_file, "w"))

    config.remove_option('nginx', 'info')  # 删除[nginx]下指定的'info' option
    config.write(open(new_config_file, "w"))
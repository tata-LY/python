#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:30
# @Author  : liuyang
# @File    : 13.2_module_configparser.py
# @Software: PyCharm

"""
python從conf里读取配置信息
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
config = configparser.ConfigParser()

if os.path.exists(config_file):
    config.read(config_file)
    print(config.defaults())    # {'serveraliveinterval': '45', 'compression': 'yes', 'compressionlevel': '9', 'forwardx11': 'yes'}
    for key,value in config.defaults().items():
        print(key,value, end=' | ') # serveraliveinterval 45 | compression yes | compressionlevel 9 | forwardx11 yes |
    print('')
    print(config.defaults()['serveraliveinterval'])     # 45

    print(config.sections())    # ['bitbucket.org', 'topsecret.server.com'] 不包括DEFAULT

    print(config['bitbucket.org']['User'])  # admin

    print(config['topsecret.server.com']['host_port'])  # 50022
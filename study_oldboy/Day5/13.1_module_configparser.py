#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:25
# @Author  : liuyang
# @File    : 13.1_module_configparser.py
# @Software: PyCharm

import configparser

# python生成一个conf文档

config_file = "13_configparser1.conf"

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'admin'
config['bitbucket.org']['Password'] = 'admin'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host_Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

print(config)   # <configparser.ConfigParser object at 0x0000018ABB0627C0>
with open(config_file, 'w') as f_w:
    config.write(f_w)

"""
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
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# python從conf里读取配置信息
# [DEFAULT]
# serveraliveinterval = 45
# compression = yes
# compressionlevel = 9
# forwardx11 = yes
#
# [bitbucket.org]
# user = admin
# password = admin
#
# [topsecret.server.com]
# host port = 50022
# forwardx11 = no

import configparser
import os

config_file = "configparser1.conf"
config = configparser.ConfigParser()

if os.path.exists(config_file):
    config.read(config_file)
    print(config.defaults())
    for key,value in config.defaults().items():
        print(key,value)
    print(config.defaults()['serveraliveinterval'])

    print(config.sections())
    print(config['bitbucket.org']['User'])

    print(config['topsecret.server.com']['host port'])

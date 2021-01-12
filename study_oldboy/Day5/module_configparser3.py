#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# python configparser增删改查语法
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
new_config_file = 'configparser2.conf'
config = configparser.ConfigParser()

if os.path.exists(config_file):
    config.read(config_file)
    config.remove_section('bitbucket.org')  # 删除[bitbucket.org]所有配置
    config.write(open(new_config_file, 'w'))

    print(config.has_section('nginx'))
    config.add_section('nginx')
    config.write(open(new_config_file, 'w'))

    config['nginx']['IP'] = "172.25.2.7"
    config['nginx']['PORT'] = "80"
    config['nginx']['version'] = "1.9.1"
    config['nginx']['info'] = "test"
    config.write(open(new_config_file, "w"))

    config.remove_option('nginx', 'info')  # 删除[nginx]下指定的'info' option
    config.write(open(new_config_file, "w"))
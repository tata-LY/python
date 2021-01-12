#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import configparser

# python生成一个conf文档

config_file = "configparser1.conf"

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'admin'
config['bitbucket.org']['Password'] = 'admin'


config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open(config_file, 'w') as f_w:
    config.write(f_w)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 14:06
# @Author  : liuyang
# @File    : settings.py
# @Software: PyCharm

hosts = {
    'LB': [
        {'ip': '10.5.3.11', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'}
    ],
    'LOCAL': [
        {'ip': '10.5.3.12', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'},
        {'ip': '10.5.3.13', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'},
        {'ip': '10.5.3.14', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'}
    ],
    'TEST': [
        {'ip': '10.5.3.15', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'},
        {'ip': '10.5.3.16', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'},
        {'ip': '10.5.3.17', 'port': 22, 'username': 'root', 'password': 'Liuyang@2021'}
    ]
}

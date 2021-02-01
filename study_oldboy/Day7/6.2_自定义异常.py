#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 15:45
# @Author  : liuyang
# @File    : 6.2_自定义异常.py
# @Software: PyCharm

class LiuyangError(Exception):
    def __init__(self, msg):
        self.message = msg

    # def __str__(self):
    """定义了__str__，后面e=return的值"""
    #     return "数据库真的连接不上"

try:
    raise LiuyangError('数据库连不上')
except LiuyangError as e:
    print(e)        # 数据库连不上
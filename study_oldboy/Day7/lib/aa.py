#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 10:49
# @Author  : liuyang
# @File    : aa.py
# @Software: PyCharm

class C(object):
    def __init__(self):
        self.name = 'Alex'

    def __call__(self, *args, **kwargs):
        print("runing call", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name
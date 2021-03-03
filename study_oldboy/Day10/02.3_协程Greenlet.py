#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 16:29
# @Author  : liuyang
# @File    : 02.3_协程greenlet.py
# @Software: PyCharm

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()


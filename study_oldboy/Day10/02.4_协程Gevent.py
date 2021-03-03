#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-3 8:53
# @Author  : liuyang
# @File    : 02.4_协程Gevent.py
# @Software: PyCharm

import gevent

def foo():
    print("Running in foo")
    gevent.sleep(3)
    print("Explicit context switch to foo again")

def bar():
    print("Explict context to bar")
    gevent.sleep(2)
    print("Implicit context switch back to bar")

def goo():
    print("running in goo")
    gevent.sleep(1)
    print("running goo again")

gevent.joinall(
    [
        gevent.spawn(foo),
        gevent.spawn(bar),
        gevent.spawn(goo)
    ]
)

"""
Running in foo
Explict context to bar
running in goo
running goo again
Implicit context switch back to bar
Explicit context switch to foo again
"""

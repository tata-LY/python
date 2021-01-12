#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 函数即变量
def test1():
    print("in the test1")

def bar(func):
    func()
    print("in the bar")

bar(test1)
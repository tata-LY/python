#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 嵌套函数

def foo():
    print("in the foo")
    def bar():
        print("in the bar")

    bar()

foo()

x = 0
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()
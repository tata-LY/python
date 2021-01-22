#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 15:55
# @Author  : liuyang
# @File    : 10.py
# @Software: PyCharm

name = "Liuyang"


def change_name():
    name = "Liuyang2"

    def change_name2():
        name = "Liuyang3"
        print("第3层打印", name)

    change_name2()  # 调用内层函数
    print("第2层打印", name)


change_name()
print("最1层打印", name)
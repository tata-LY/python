#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-8 14:56
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm
"""
练习1：在屏幕上显示跑马灯文字。
"""
import time

def main():
    content = "肥肥仔菜花喵编剧小能手....."
    while True:
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
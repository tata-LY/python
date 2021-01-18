#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 10:54
# @Author  : liuyang
# @File    : shopping.py
# @Software: PyCharm

import os
import sys

# 把当前项目加入到Python path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import common, manager, consumer


def main():
    option = {
        '1': '商场用户',
        '2': '消费者',
        'q': '退出系统'
    }

    while True:
        choice = common.choice(option)
        if choice == '1':
            manager.main()
        elif choice == '2':
            consumer.main()
        elif choice == 'q':
            exit("欢迎下次光临！")

if __name__ == '__main__':
    main()
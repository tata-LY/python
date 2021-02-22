#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-26 14:12
# @Author  : liuyang
# @File    : 打印目录机构.py
# @Software: PyCharm

import os
import os.path

dir_name = r'D:\刘洋工作\20200921\git\python\study_oldboy\Day8\work'


def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "|--" + item)

            newitem = path + '/' + item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth + 1)


if __name__ == '__main__':
    dfs_showdir(dir_name, 0)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-1 9:35
# @Author  : liuyang
# @File    : 目录总大小.py
# @Software: PyCharm

import os, re

dir = 'E:/刘洋工作/20200921/git/tata-LY/python/study_oldboy/Day8'


def dir_file_size(path):
    if os.path.isdir(path):
        file_size, dir_list = 0, [path]
        while dir_list:
            path = dir_list.pop()
            dirs = os.listdir(path)
            for name in dirs:
                file_path = os.path.join(path, name)
                if os.path.isfile(file_path):
                    file_size += os.path.getsize(file_path)
                else:
                    dir_list.append(file_path)
        return file_size
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:
        print('找不到%s文件' % path)

print(dir_file_size(dir))
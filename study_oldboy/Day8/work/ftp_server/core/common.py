#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-22 9:00
# @Author  : liuyang
# @File    : common.py
# @Software: PyCharm

import os

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

pass

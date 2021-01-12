#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

dir_path = "C:/Users/Administrator/Desktop/煜顺工控/淘宝图片/三菱"
files = file_name(dir_path)
for name in files:
    print(name)
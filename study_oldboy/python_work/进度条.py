#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-22 11:14
# @Author  : liuyang
# @File    : 进度条.py
# @Software: PyCharm
import math
import sys
import time


def progressbar(cur, total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ('=' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')


if __name__ == '__main__':
    file_size = 102400
    size = 0
    while size <= file_size:
        progressbar(size, file_size)
        size += 1024
        time.sleep(0.5)     # 增加sleep，可以看出效果
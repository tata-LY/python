#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 15:18
# @Author  : liuyang
# @File    : main.py
# @Software: PyCharm

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    main.run()
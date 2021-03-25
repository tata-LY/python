#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-23 10:22
# @Author  : liuyang
# @File    : start.py
# @Software: PyCharm

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main
main.run()
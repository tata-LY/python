#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

print("in package package_test!")

# import package1       # 不可行
from . import package1  # '.'代表__init__.py的当前路径
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import module1
import sys
import os

module1.sayhi("ly")

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
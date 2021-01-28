#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import module1
from module1 import sayhi   # 模块调用优化，不再需要每次去module1里找
import sys
import os

module1.sayhi("ly")
for i in range(10):
    sayhi(i)    # 直接调用sayhi函数，不再需要每次去module1里找


print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
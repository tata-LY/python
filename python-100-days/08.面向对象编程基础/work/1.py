#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-12 16:24
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm
"""
练习1：定义一个类描述数字时钟。
"""

import time
import os
import sys

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        """时间显示"""
        print('%02d:%02d:%02d' % (self.hour, self.minute, self.second))

    def run(self):
        """时间走动"""
        time.sleep(1)
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                if self.hour == 23:
                    self.hour =0
                else:
                    self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1

def main():
    clock1 = Clock(23, 59, 59)
    while True:
       # os.system("clear")  # Linux支持
        clock1.show()
        clock1.run()

if __name__ == '__main__':
    main()












































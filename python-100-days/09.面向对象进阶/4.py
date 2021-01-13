#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-13 10:02
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm

"""
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
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

    @classmethod
    def now(cls):
        ctime = time.localtime()
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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
    clock1 = Clock.now() # 通过类方法创建对象并获取系统时间
    while True:
       # os.system("clear")  # Linux支持
        clock1.show()
        clock1.run()

if __name__ == '__main__':
    main()
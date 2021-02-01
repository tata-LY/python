#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 10:24
# @Author  : liuyang
# @File    : 3.2_属性方法例子.py
# @Software: PyCharm

class Flight(object):
    """这个类是查看航班状态"""
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        """检查航班状态"""
        print("checking flight %s status " % self.flight_name)
        return  0

    @property
    def flight_status(self):
        status = self.checking_status() # 获取航班状态
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")
    @flight_status.setter
    def flight_status(self,status):
        print("flight %s has changed status to %s" %(self.flight_name,status))

f = Flight("CA980")
f.flight_status
"""
checking flight CA980 status 
flight got canceled...
"""
f.flight_status = 2     # flight CA980 has changed status to 2


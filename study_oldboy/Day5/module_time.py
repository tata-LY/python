#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import time
import datetime

print(time.time()/3600/24/365+1970)  # 时间戳，linux诞生与1970

print(time.localtime())  # UTC+8
# time.struct_time(tm_year=2018, tm_mon=10, tm_mday=9, tm_hour=1, tm_min=17, tm_sec=30, tm_wday=1, tm_yday=282, tm_isdst=0)

print(time.localtime().tm_year)

print(time.gmtime())   # UTC时间

print(time.time())
print(time.mktime(time.localtime()))  # tuple to 时间戳

print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))  # 格式化时间

print(time.strptime('2018-10-09 09-16-51', "%Y-%m-%d %H-%M-%S"))   # 格式化时间转成时间tuple

print(time.asctime()) # tuple >>> Tue Oct  9 09:25:14 2018
print(time.localtime())
print(time.asctime(time.localtime()))

print(time.ctime())   # 时间戳 >>> Tue Oct  9 09:25:14 2018
print(time.time())
print(time.ctime(time.time()))

print(datetime.datetime.now())  # 当前时间 2018-10-09 09:34:09.616093
print(datetime.datetime.now()+datetime.timedelta(3))  # 三天后
print(datetime.datetime.now()+datetime.timedelta(-3)) # 三天前
print(datetime.datetime.now()+datetime.timedelta(hours=-3)) # 三小时前
print(datetime.datetime.now()+datetime.timedelta(minutes=3)) # 三分钟后
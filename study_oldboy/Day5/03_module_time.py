#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import time
import datetime

print(time.time())  # 1611717615.5555413 时间戳，linux诞生与1970
print(time.time()/3600/24/365+1970) # 2021.1072303258525
print(time.localtime())  # UTC+8    # time.struct_time(tm_year=2021, tm_mon=1, tm_mday=27, tm_hour=11, tm_min=20, tm_sec=15, tm_wday=2, tm_yday=27, tm_isdst=0)

print(time.localtime().tm_year)   # 2021

print(time.gmtime())   # UTC(国际协调时)时间  time.struct_time(tm_year=2021, tm_mon=1, tm_mday=27, tm_hour=3, tm_min=22, tm_sec=23, tm_wday=2, tm_yday=27, tm_isdst=0)

print(time.time())  # 1611717743.5676389
print(time.mktime(time.localtime()))  # 1611717743.0 tuple to 时间戳

print( time.strftime("%Y-%m-%d %H-%M-%S"))  #  2021-01-27 13-28-14
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))  # 2021-01-27 11-23-54 格式化时间转换

print(time.strptime('2018-10-09 09:16:51', "%Y-%m-%d %H:%M:%S"))   # 格式化时间转成时间tuple time.struct_time(tm_year=2018, tm_mon=10, tm_mday=9, tm_hour=9, tm_min=16, tm_sec=51, tm_wday=1, tm_yday=282, tm_isdst=-1)

print(time.asctime()) # tuple >>> Wed Jan 27 11:24:41 2021
print(time.localtime()) # time.struct_time(tm_year=2021, tm_mon=1, tm_mday=27, tm_hour=11, tm_min=24, tm_sec=41, tm_wday=2, tm_yday=27, tm_isdst=0)
print(time.asctime(time.localtime()))   # Wed Jan 27 11:26:44 2021

print(time.ctime())   #Wed Jan 27 11:26:44 2021
print(time.time())  # 1611718004.4909644
print(time.ctime(time.time()))  # Wed Jan 27 11:26:44 2021

print(datetime.datetime.now())  # 当前时间 2021-01-27 11:27:36.396441
print(datetime.datetime.now()+datetime.timedelta(3))  # 三天后 2021-01-30 11:27:36.396441
print(datetime.datetime.now()+datetime.timedelta(-3)) # 三天前 2021-01-24 11:27:36.396441
print(datetime.datetime.now()+datetime.timedelta(hours=-3)) # 三小时前  2021-01-27 08:27:36.396441
print(datetime.datetime.now()+datetime.timedelta(minutes=3)) # 三分钟后 2021-01-27 11:30:36.396441
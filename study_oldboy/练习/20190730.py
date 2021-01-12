#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os, sys
import datetime

pwd_dir = os.getcwd()
info_file = os.path.join(pwd_dir, 'info.txt')

now_date = datetime.datetime.now().strftime('%Y-%m-%d')
if not os.path.isfile(info_file):
    f_w = open(info_file, "w")
    f_w.close()

name = input("Name：")
age = int(input("Age: "))

info = """INFO of {_name}
Name:{_name}
Age:{_age}""".format(_name=name, _age=age)

with open(info_file, "w", encoding="utf8") as f_w:
    f_w.write(now_date)
    f_w.write("\n" + info)
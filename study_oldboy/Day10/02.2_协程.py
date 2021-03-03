#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 16:14
# @Author  : liuyang
# @File    : 02.2_协程.py
# @Software: PyCharm

import time

def home():
    print("in the home")
    time.sleep(5)   # get data from db
    print("home exec done...")

def bbs():
    print("in the bbs")
    time.sleep(2)

def login():
    print("in the login")

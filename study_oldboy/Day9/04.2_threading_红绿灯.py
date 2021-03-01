#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 16:01
# @Author  : liuyang
# @File    : 04.2_threading_红绿灯.py
# @Software: PyCharm

import threading, time
import random



def lighter():
    count = 21
    while True:
        if 0 < count <= 10:      # 绿灯
            print("\033[42;1m--green light on---\033[0m")
        if 10 < count <= 13:      # 黄灯
            print("\033[43;1m--yellow light on---\033[0m")
        elif 13 < count <= 20:    # 红灯
            event.clear()       # 关闭绿灯，打开红灯标识
            print("\033[41;1m--red light on---\033[0m")
        elif count > 20:
            event.set()     # 打开绿灯
            count = 0

        time.sleep(1)
        count += 1

def car(n):
    while True:
        time.sleep(random.randint(1, 10))
        if event.isSet():   # 绿灯running
            print("car is running..")
        else:       # 红灯waiting
            print("car is waiting for red light...")
            event.wait()
            print("green light is on, start going...")

if __name__ == '__main__':
    event = threading.Event()
    light = threading.Thread(target=lighter)
    light.start()
    for i in range(3):
        t = threading.Thread(target=car, args=(i, ))
        t.start()
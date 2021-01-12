#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


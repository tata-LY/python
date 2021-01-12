#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

'''


for i in range(0,10,3):
    print("loop ",i)

'''

for i in range(10):
    print("--------",i)
    for j in range(10):
        if j == 5:
            continue
        print(j)
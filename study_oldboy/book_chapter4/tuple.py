#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

tuple1 = (1,100)
print(tuple1)
print(tuple1[0])

#tuple1[0] = 10   #元组不允许修改
#print(tuple1)

for i in tuple1:
    print(i)

tuple1 = ('liuyang', 'zhangjuan')   # 不允许修改，可以重新定义
print(tuple1)

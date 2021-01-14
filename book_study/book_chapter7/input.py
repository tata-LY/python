#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

print(5 % 2)

num = int(input("Please enter a number: "))   #输入的都是str类型

if num % 2 == 0 :
    print("the number {num} is even.".format(num=num))
else:
    print("the number {num} is odd.".format(num=num))

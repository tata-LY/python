#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

while True:
    number = int(input("Please input a odd number: "))
    if number % 2 != 0:
        print("The input number {num} is odd.".format(num=number))
        break
    else:
        print("The number is even, Please input again!")


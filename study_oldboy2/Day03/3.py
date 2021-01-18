#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-15 10:35
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm

death_age = 80


name = input("your name:")
age = input("your age:")  #input 接受的所有数据都是字符串，即便你输入的是数字，但依然会被当成字符串来处理

print( type(age) )


#int integer =整数  把字符串转成int,用int(被转的数据)
#str string =字符串 把数据转成字符串用str(被转的数据)
print("Your name:",name)
#print("You can still live for ",  death_age - int(age)," years ....")
print("You can still live for " +  str(death_age - int(age)) +" years ....")
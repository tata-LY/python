#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-15 10:42
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm

age_of_princal = 56



guess_age = int(   input(">>:") )
'''
if guess_age == age_of_princal then

	print("yes")
else 
	print("no ")
'''

if guess_age == age_of_princal:
    print("Yes,you got it..")
elif guess_age > age_of_princal:
    print("shoud try samller..")
else:
    print("try bigger ...")
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

age_of_oldboy = 56

while True:
    guess_age = int(input("guess age:"))


    if guess_age == age_of_oldboy:
        print("Yes, you got it. ")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller...")
    else:
        print("Think bigger...")

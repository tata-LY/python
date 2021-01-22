#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

count = 0
guess_num=3
age_of_oldboy = 56
while count < guess_num:
    count = count + 1
    guess_age = int(input("guess_age:"))
    if guess_age == age_of_oldboy:
        print("Yes, you got it. ")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller ...")
    else:
        print("Think bigger ...")
else:
    print("You tries too many times, fuck off! ")
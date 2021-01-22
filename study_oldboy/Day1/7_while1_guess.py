#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

count = 0
guess_num=3
age_of_oldboy = 56
while True:
    count = count + 1
    guess_age = int(input("guess_age:"))
    if guess_age == age_of_oldboy:
        print("Yes, you got it. ")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller ...")
    else:
        print("Think bigger ...")

    if count == guess_num:
        contiue_confirm = input("You have ties {guess_num} times, Do you wanted to keep guessing".format(guess_num=guess_num))
        if contiue_confirm != "n":
            count = 0
        else:
            print("Fuck off! ")
            break

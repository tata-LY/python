#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-12 15:21
# @Author  : liuyang
# @File    : z2.py
# @Software: PyCharm

"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
实现思路：
30 * True，Fasle表示掉入海里的非基督教的。True就计数，Fasle不计数，到9就把True=Fasle，总共循环15次。
"""

def main():
    persons = [True] * 30
    count = 0
    num = 0
    index = 0
    while count < 15:
        if persons[index]:  # false就是已经掉入海里的，不计数
            num += 1
            if num == 9:
                persons[index] = False
                num = 0
                count += 1
        index += 1
        index = index % 30
    print(persons)
if __name__ == '__main__':
    main()
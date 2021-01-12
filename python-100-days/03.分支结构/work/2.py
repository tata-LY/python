#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 11:23
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

# 练习2：百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E
score = float(input("Please input your score: "))
if 80 <= score < 90:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
elif score < 60:
    grade = "E"

print("Your grade is : %s" % grade)
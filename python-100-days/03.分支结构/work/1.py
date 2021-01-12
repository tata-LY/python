#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 11:00
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

# 练习1：英制单位英寸与公制单位厘米互换。
# 英寸 / 厘米 = 2.54

value = float(input("输入长度："))
unit = input("输入单位：")
if unit == "in" or unit == "英寸":
    print("%f英寸 = %f厘米" % (value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("%f厘米 = %f英寸" % (value, value/2.54))
else:
    print("请输入合法的单位！")
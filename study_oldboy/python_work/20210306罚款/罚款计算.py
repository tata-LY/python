#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-6 11:28
# @Author  : liuyang
# @File    : 罚款计算.py
# @Software: PyCharm

info = """
总罚款10000元，8个人按照业绩比例罚款，与业绩成反比。
8人业绩：10%,10%,15%,12%,18%,5%,20%,10%
计算结果如下：
"""

print(info)

sum = 10000     # 总罚款额
yeji = [10, 10, 15, 12, 18, 5, 20, 10]      # 业绩比例

jishu = 10  # 罚款份额基数比例
yeji_fk_b = [jishu/i for i in yeji]     # 计算每个人多少基数倍罚款
print(yeji_fk_b)

fene_b = 0
for i in yeji:
    fene_b += jishu/i
fene_fk = sum/fene_b        # 罚款份额基数比例所罚金额
print(fene_fk)

index = 1
for item in yeji_fk_b:
    fk = fene_fk * item     # 每个人的罚款金额 = 罚款份额基数比例所罚金额 * 每个人多少基数倍罚款
    print("第%d个人，业绩%.2f,罚款额为%f" % (index, yeji[index-1]/100, fk))
    index += 1

#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import random

print(random.random())  # 0-1
print(random.randint(1,10)) # 1-10 int
print(random.randrange(3)) # 0-2
print(random.randrange(1,3)) # 1-2
print(random.choice("abcdefg")) # 字符串中选择一个
print(random.choice([1,2,3,4,5,6,7,8]))
print(random.uniform(1,10)) # 1-10 float

l = [1,2,3,4,5,6,7,8]
random.shuffle(l)  # 打乱顺序
print(l)

# 生产随机验证码
check_code = ''
for i in range(5):
    current = random.randrange(0,4)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = str(random.randint(0,9))
    check_code += str(tmp)

print(check_code)
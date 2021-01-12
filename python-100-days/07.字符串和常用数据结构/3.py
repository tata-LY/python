#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-8 10:44
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm
"""
列表生成式和生成器
"""
import sys
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'abc' for y in '12345']
print(f)
f = [x ** 2 for x in range(1, 10)]
print(f)
print(sys.getsizeof(f)) # 查看对象占用内存的字节数
for val in f:
    print(val)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

print(fib(10))
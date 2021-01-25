#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 15:50
# @Author  : liuyang
# @File    : 10.1_generator生成器.py
# @Software: PyCharm

def test(num=0):
    result = num * 2
    return result
generator1 = (test(i) for i in range(10))
print(generator1) # <generator object <genexpr> at 0x0000014E488163C0>

# 取完后后面就取不到了
for i in generator1:
    print(i, end=' ') # 0 2 4 6 8 10 12 14 16 18
print('')

generator2 = (i*2 for i in range(10))
# 一个一个取
print(generator2.__next__()) # 0    取第一个
print(generator2.__next__()) # 2    取第二个
print(generator2.__next__()) # 4    取第三个

# 斐波那契
print("斐波那契".center(30, '-'))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=' ')
        a, b = b, a+b
        n = n + 1
fib(10) # 1 1 2 3 5 8 13 21 34 55
print('')

# 斐波那契生成器
print("yield生成生成斐波那契器".center(30, '-'))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b     # yield把b追加到一个生成器里
        a, b = b, a+b
        n = n + 1
    return "done"   # return不会被返回了

print(fib(10))  # <generator object fib at 0x00000210CE708F20>
fib_gen1 = fib(10)

print(fib_gen1.__next__()) # 1
print(fib_gen1.__next__()) # 1
print(fib_gen1.__next__()) # 2
# 打印剩下的
for i in fib_gen1:
    print(i, end=' ')       # 3 5 8 13 21 34 55
print('')

fib_gen2 = fib(5)
while True:
    try:
        x = next(fib_gen2)
        print("fib_gen1: ", x, end=' | ') # fib_gen1:  1 | fib_gen1:  1 | fib_gen1:  2 | fib_gen1:  3 | fib_gen1:  5 |
    except StopIteration as e:
        print('\nGenerator return value: ', e.value) # Generator return value:  done   会打印result的值
        break

# 排序
data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]
data2 = data.copy()
print("before sort:", data)previous = data[0]
for j in range(len(data)):
    tmp = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
    print(data)

print("after sort:", data)  # [1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 17, 21, 22, 33, 54]
print(sorted(data2))    # [1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 17, 21, 22, 33, 54]
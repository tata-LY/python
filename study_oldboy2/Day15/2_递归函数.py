#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 16:28
# @Author  : liuyang
# @File    : 2_递归函数.py
# @Software: PyCharm

def calc(n):
    print(n)
    if int(n/2) >0:
        return calc( int(n/2) )
    print("->",n)
calc(10)


# 阶乘
print('阶乘'.center(30, '*'))
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result
print('阶乘：' ,factorial(4))


def factorial_new(n):
    if n == 1:
        return 1
    return n * factorial_new(n - 1)
print('递归实现阶乘：' ,factorial_new(4))


print('斐波那契数列'.center(30, '*'))
def fibo(n):
    before = 0
    after = 1
    for i in range(n - 1):
        ret = before + after
        before = after
        after = ret
        print(ret, end=' ')

    return ret
print('总和：' ,fibo(10))


def fibo_new(n):  # n可以为零，数列有［0］
    if n <= 1:
        return n
    return (fibo_new(n - 1) + fibo_new(n - 2))
print('总和：' ,fibo_new(10))
# f(1)=0,f(2)=1,f(3)=f(1)+f(2)=1,f(4)=f(2)+f(3)=2,f(5)=f(3)+f(4)=3,...,f(10)=f(8)+f(9)


def sum(n): # 1-10和
    if n == 1:
        return n
    return n + sum(n-1)

print(sum(10))
# sum(10) = 10 + sum(9) = 10 + 9 + sum(8) = 10 +9 + 8 + sum(7) = ... = 10+9+8+7+...+1
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 15:14
# @Author  : liuyang
# @File    : 8_def_复杂传参.py
# @Software: PyCharm

# *args:接受N个位置参数，转换成元组形式
print('*args传参'.center(30, '*'))
def test(*args):
    print(args)

test(1,2,3,4,5,5)
test(*[1,2,4,5,5])#  args=tuple([1,2,3,4,5])

def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,7)


#**kwargs：接受N个关键字参数，转换成字典的方式
print('**kwargs传参'.center(30, '*'))
def test2(**kwargs):
    print(kwargs)

test2(name='liuyang',age=8,sex='F')
test2(**{'name':'liuyang','age':8})
# test2({'name':'liuyang','age':8}) # 错误传参：TypeError: test2() takes 0 positional arguments but 1 was given

def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3(name='liuyang',age=18,sex='m')

def test4(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test4(name='liuyang',age=34,sex='m',hobby='tesla')


print('*args传参 **kwargs传参'.center(30, '*'))
def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")

def logger(source):
    print("from %s" %  source)

test4('liuyang',1,2,3,sex='m',hobby='tesla') # name='liuyang', age=1, args=(2,3), kwargs = {'sex': 'm', 'hobby': 'tesla'}


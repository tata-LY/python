#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-13 8:58
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm
"""
访问可见性问题
对于上面的代码，有C++、Java、C#等编程经验的程序员可能会问，我们给Student对象绑定的name和age属性到底具有怎样的访问权限（也称为可见性）。因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不允许外界访问，而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的消息。在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
"""

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

    def use_pri(self):
        print(self.__foo)

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar() # 不能调用私有的
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo) # 不能条用私有的
    test.use_pri()

if __name__ == "__main__":
    main()
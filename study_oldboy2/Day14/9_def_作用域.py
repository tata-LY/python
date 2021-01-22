#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 15:35
# @Author  : liuyang
# @File    : 9_def_局部变量.py
# @Software: PyCharm

"""
全局与局部变量

在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
当全局变量与局部变量同名时：
在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。

（1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；

（2）只有模块、类、及函数才能引入新作用域；

（3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；

（4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。
"""

school = "Oldboy edu."
names = ["Alex","Jack","Rain"]
names_tuple = (1,2,3,4)
def change_name1():
    names[0] = "tata"

    print("inside func",names)
change_name1()
print(names)


print('----------------------')

def change_name2(name):
    global school   # 会修改全局变量
    school = "Mage Linux"
    print("before change",name,school)
    name ="Liuyang" #这个函数就是这个变量的作用域
    age =23
    print("after change",name)

print("school:",school)
name = "alex"
change_name2(name)
print(name)
print(school)

# print("age",age)

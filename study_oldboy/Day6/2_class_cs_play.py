#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-28 15:11
# @Author  : liuyang
# @File    : 2_class_cs_play.py
# @Software: PyCharm

class Role(object):
    n = 123 # 类变量，大家公有的属性，节省开销
    name = "我是类name"
    n_list = [1, 2]

    def __init__(self, name, role, weapon, life_value=100, money=10000):
        """
        构造函数
        在实例化时做一些类的初始化工作
        """
        self.name = name    # 实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value      # 私有属性，外面调用不了
        self.money = money

    def __del__(self):
        """析构函数：在实例释放、销毁的时候自动执行的，通常做一些收尾工作。比如关闭数据库连接、关闭打开的临时文件。"""
        self.__print("%s 彻底死了......" % self.name)

    def __print(self, data):
        """私有方法，只能内部调用   调用：self.__print"""
        print("\033[31;1m{data}\033[0m".format(data=data))

    def shot(self): # 类的方法，功能（动态属性）
        self.__print("Shooting...biu biu biu")

    def show_status(self):
        self.__print("name: {name}, life_value: {life_value}".format(name=self.name, life_value=self.__life_value))

    def got_shot(self):
        self.__print("%s：ah..., I got shot..." % self.name)
        self.__life_value -= 10     # 中枪后生命值-10

    def buy_gun(self, gun_name):
        self.__print("%s just bought %s" % (self.name, gun_name))
        self.weapon = gun_name

r1 = Role('Ronnie', 'police', 'AK47')       # 类生成一个对象，类Role的实例化（初始化）
r2 = Role('Liuyang','police','B15')         # 类生成一个对象，类Role的实例化（初始化）
r3 = Role('Zhangjuan','police','B15')       # 类生成一个对象，类Role的实例化（初始化）


print(Role.n)           # 123 类变量，存在类的内存里
print(r1.n, r1.name, r1.weapon)    # 123 Ronnie AK47    r1.name先找实例变量再找类变量
print(r2.n, r2.name, r2.weapon)    # 123 Liuyang B15

r1.got_shot()
r1.buy_gun('BBB15')     # self.name = gun_name = 'BBB15'
print(r1.name, r1.weapon)       # Ronnie BBB15

r2.name = 'Tata'
print(r1.name, r2.name) # Ronnie Tata r2.name已经被修改

r1.bullet_prove = True  # r1增加一个新的属性bullet_prove(防弹衣)
print(r1.name, r1.bullet_prove, r1.weapon)     # Ronnie True BBB15

del r1.weapon       # 删除r1的属性weapon
# print(r1.name, r1.bullet_prove, r1.weapon)  # AttributeError: 'Role' object has no attribute 'weapon'

r1.n = "修改类变量" # 只会修改r1的
print(r1.n, r1.name)        # 修改类变量 Ronnie
print(r2.n, r2.name)        # 123 Tata

Role.n = "全局修改"
print(r1.n, r1.name)        # 修改类变量 Ronnie 修改过的r1.n不会再被改了
print(r2.n, r2.name)        # 全局修改 Tata
print(r3.n, r3.name)        # 全局修改 Zhangjuan

r1.n_list.append("from r1")
r2.n_list.append("from r2")
print(r1.n_list, r2.n_list, Role.n_list)   # [1, 2, 'from r1', 'from r2'] [1, 2, 'from r1', 'from r2'] [1, 2, 'from r1', 'from r2'] 使用的Role里面n_list列表内存地址一致

r3.n_list = ['r3修改']
print(r1.n_list, r2.n_list, r3.n_list, Role.n_list)     # [1, 2, 'from r1', 'from r2'] [1, 2, 'from r1', 'from r2'] ['r3修改'] [1, 2, 'from r1', 'from r2'] 这样是跟修改变量一样。

r1.buy_gun("B15")   # Ronnie just bought B15
r1.got_shot()       # Ronnie：ah..., I got shot...
del r1              # 销毁r1后析构函数就会执行

r2.buy_gun("B16")   # Tata just bought B16
r2.got_shot()       # Tata：ah..., I got shot...

r2.show_status()    # name: Tata, life_value: 90
r2.got_shot()       # Tata：ah..., I got shot...
r2.show_status()    # name: Tata, life_value: 80

"""
最后析构函数__del__执行结果：
Ronnie 彻底死了......
Tata 彻底死了......
Zhangjuan 彻底死了......
"""
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

class Role:
    n = 123  # 类变量，大家公有的属性，节省开销
    n_list = [1, 2]
    name = "Role name"
    def __init__(self, name, role, weapon, life_value=100, money=10000):
        # 构造函数
        # 在实例化时做一些类的初始化工作
        self.name = name   # 实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        # self.life_value = life_value
        self.__life_value = life_value  # 私有属性，外面调用不了
        self.money = money

    def __del__(self):
        # 析构函数：在实例释放、销毁的时候自动执行的，通常做一些收尾工作。比如关闭数据库连接、关闭打开的临时文件。
        self.__print("析构函数最后执行：%s 彻底死了 ... " %self.name)

    def __print(self, data):
        # 私有方法，只能内部调用   调用：self.__print
        print("\033[31;1m{data}\033[0m".format(data=data))

    def shoted(self): # 类的方法，功能（动态属性）
        self.__print("shotting, biu biu biu ...")

    def show_status(self):
        self.__print("name: {name}, life_value: {life_value}".format(name=self.name, life_value=self.__life_value))

    def got_shot(self):
        self.__print("{who}: ah ..., I got shot ...".format(who=self.name))
        self.__life_value -= 10

    def buy_gun(self, gun_name):
        self.__print("{who} bought {gun_name}".format(who=self.name, gun_name=gun_name))

print(Role.n, Role.name)

r1 = Role('Ronnie','police','AK47')  # 类生成一个对象，类Role的实例化（初始化）
r2 = Role('Liuyang','police','B15')  # 类生成一个对象，类Role的实例化（初始化）
r3 = Role('test','police','B15')  # 类生成一个对象，类Role的实例化（初始化）
# r1.buy_gun("B15")
# r1.got_shot()
print(r1.n, r1.name)   # 先找实例变量，再找类变量
print(r2.n, r2.name)

r2.name = "TaTa"
r2.buy_gun('AK47')

r1.bullet_prove = True
print(r1.name, r1.bullet_prove, r1.weapon)
del r1.weapon
# print(r1.name, r1.bullet_prove, r1.weapon)

r1.n = "修改类变量" # 只会修改r1的
print(r1.n, r1.name)
print(r2.n, r2.name)

Role.n = "全局修改"
print(r1.n, r1.name)  # 修改过的r1.n不会再被改了
print(r2.n, r2.name)
print(r3.n, r3.name)

r1.n_list.append("from r1")
r2.n_list.append("from r2")
print(r1.n_list, r2.n_list, Role.n_list)   # 使用的Role n_list 内存地址一致


r1.buy_gun("B15")
r1.got_shot()
# del r1   # 删除r1后析构函数就会执行

r2.buy_gun("B16")
r2.got_shot()

r2.show_status()
r2.got_shot()
r2.show_status()
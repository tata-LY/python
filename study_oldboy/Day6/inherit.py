#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# class People():  # 经典类
class People(object):  # 新式类（多继承变了）
    def __init__(self, name, age, ):
        self.name = name
        self.age = age
        self.friends = []

    def __print(self, data):
        # 私有方法，只能内部调用   调用：self.__print
        print("\033[31;1m{data}\033[0m".format(data=data))

    def eat(self):
        self.__print("%s is eating ..." % self.name)

    def sleep(self):
        self.__print(("%s is sleeping ..." % self.name))

    def show_info(self):
        self.__print("name: {name}, age: {age}".format(name=self.name, age=self.age))

class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj)

class Man(People, Relation):
    # 继承
    def __init__(self, name, age, money):
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)   # 与上面效果一样（新式类写法）
        self.money = money
        print("%s一出生就有%s块钱" % (self.name, self.money))

    def talk(self):
        print(("%s is talking ..." % self.name))  # 私有方法不能继承

    def sleep(self):
        # 重构父类
        # People.sleep(self)
        super(Man, self).sleep()   # 与上面效果一样
        print("man is sleeping")

class Women(People, Relation):
    # 继承
    def get_birth(self):
        print("%s is borning a baby ... " % self.name)

m1 = Man("LiuYang", 27, 100)
m1.show_info()
m1.talk()
m1.sleep()

w1 = Women("ZhangJuan", 26)
w1.get_birth()
w1.show_info()

m1.make_friends(w1)
print(m1.friends[0].name)
w1.name = "张娟"
print(m1.friends[0].name)
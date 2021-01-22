#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 9:22
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

import os, linecache, time

def manager():
    info = '''
请选择您的操作：
    【1】增加商品
    【2】删除商品
    【3】修改商品
    【4】查看商品
    【b】返回
    【q】退出系统
    '''
    if not os.path.isfile(goods_file):
        f = open(goods_file, "w",encoding="UTF-8")
        f.close()

    while True:
        choice = input(info)
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                add_goods()
            elif choice == 2:
                del_goods()
            elif choice == 3:
                mod_goods()
            elif choice ==4:
                view_goods()
                input("输入任意键继续:")
            else:
                print("\033[31;1mInvalid option!\033[0m")
        elif choice == "b":
            break
        elif choice == "q":
            exit("Goodbye!")
        else:
            print("\033[31;1mInvalid option!\033[0m")

def add_goods():
    while True:
        print("请填入正确的商品信息".center(20,"-"))
        goods_name = input("商品名称: ")
        if goods_name == "":
            print("\033[31;1m输入的商品名称不能为空!\033[0m")
            continue
        goods_price = input("商品价格: ")
        if goods_price.isdigit():
            f_r = open(goods_file, "r")
            goods_info_list = f_r.readlines()
            f_r.close()
            flag = 0
            for line in goods_info_list:
                if "[" + goods_name + "]" == line.split(":")[0]:
                    flag = 1
                    continue

            if flag == 0:
                f_a = open(goods_file, "a", encoding="UTF-8")
                f_a.write("[" + goods_name + "]" + ":" + goods_price + "\n")
                f_a.close()
                print("商品\033[31;1m{goods_name}\033[0m 已添加成功".format(goods_name=goods_name))
                choice = input("是否继续添加新的商品信息【Y/N】:")
                if choice == "Y" or choice == "y":
                    pass
                else:
                    break
            else:
                print("商品\033[31;1m{goods_name}\033[0m 已经存在! ".format(goods_name=goods_name))
                choice = input("是否继续添加新的商品信息【Y/N】:")
                if choice == "Y" or choice == "y":
                    pass
                else:
                    break
        else:
            print("\033[31;1m输入的商品价格不合法，必须是一个正数!\033[0m")

def del_goods():
    while True:
        goods_len = view_goods()
        choice = input("请选择您要删除的商品[1-{goods_len}]: ".format(goods_len=goods_len))
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= goods_len:
                f_r = open(goods_file, "r", encoding="utf-8")
                goods_info_list = f_r.readlines()
                f_r.close()
                new_goods_info = ''
                for index,item in enumerate(goods_info_list):
                    if choice-1 != index:
                        new_goods_info += item
                    else:
                        del_goods_name = item.split(":")[0]
                f_w = open(goods_file, "w", encoding="utf-8")
                result = f_w.write(new_goods_info)
                f_w.close()
                if result:
                    print("\033[31;1m{del_goods_name}商品删除成功!\033[0m".format(del_goods_name=del_goods_name))
                    choice = input("是否继续删除其他商品信息【Y/N】:")
                    if choice == "Y" or choice == "y":
                        pass
                    else:
                        break
            else:
                print("\033[31;1m商品不存在!\033[0m")
                choice = input("是否继续删除其他商品信息【Y/N】:")
                if choice == "Y" or choice == "y":
                    pass
                else:
                    break
        else:
            print("\033[31;1mInvalid option!\033[0m")
            choice = input("是否继续删除其他商品信息【Y/N】:")
            if choice == "Y" or choice == "y":
                pass
            else:
                break
def mod_goods():
    while True:
        goods_len = view_goods()
        choice = input("请选择您要修改的商品[1-{goods_len}]: ".format(goods_len=goods_len))
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= goods_len:
                f_r = open(goods_file, "r", encoding="utf-8")
                goods_info_list = f_r.readlines()
                f_r.close()
                new_goods_info = ''
                for index, item in enumerate(goods_info_list):
                    if choice - 1 != index:
                        new_goods_info += item
                    else:
                        mod_goods_name = item.split(":")[0]
                        while True:
                            new_price = input(
                                "\033[31;1m{mod_goods_name}\033[0m商品新价格：".format(mod_goods_name=mod_goods_name))
                            if new_price.isdigit():
                                new_price = int(new_price)
                                item = mod_goods_name + ":" + str(new_price) + "\n"
                                new_goods_info += item
                                break
                            else:
                                print("\033[31;1m输入的{mod_goods_name}商品价格不合法，请重新输入：\033[0m".format(
                                    mod_goods_name=mod_goods_name))
                f_w = open(goods_file, "w", encoding="utf-8")
                result = f_w.write(new_goods_info)
                f_w.close()
                if result:
                    print("\033[31;1m{mod_goods_name}\033[0m商品修改成功!".format(mod_goods_name=mod_goods_name))
                    choice = input("是否继续修改其他商品信息【Y/N】:")
                    if choice == "Y" or choice == "y":
                        pass
                    else:
                        break
            else:
                print("\033[31;1m商品不存在!\033[0m")
                choice = input("是否继续修改其他商品信息【Y/N】:")
                if choice == "Y" or choice == "y":
                    pass
                else:
                    break
        else:
            print("\033[31;1mInvalid option!\033[0m")
            choice = input("是否继续修改其他商品信息【Y/N】:")
            if choice == "Y" or choice == "y":
                pass
            else:
                break
def view_goods():
    f_r = open(goods_file, "r")
    goods_info= f_r.readlines()
    goods_len=len(goods_info)
    f_r.close()
    for index,item in enumerate(goods_info):
        print(index+1,item.rstrip())
    return goods_len


def consumer():
    info = '''
    【1】购买商品
    【2】查看余额
    【b】返回
    【q】退出系统'''
    while True:
        print(info)
        choice = input("请选择>>> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                shopping()
            elif choice == 2:
                balance = view_balance(balance_file=balance_file)
                print("您现在的余额为：\033[31;1m{balance}\033[0m".format(balance=balance))
                choice = input("是否现在充值【Y/N】: ")
                if choice == "Y" or choice == "y":
                    while True:
                        add_balance = input("充值余额：")
                        if add_balance.isdigit():
                            add_balance = int(add_balance)
                            new_balance = balance + add_balance
                            f_w = open(balance_file, "w", encoding="utf-8")
                            result = f_w.write(str(new_balance))
                            f_w.close()
                            if result:
                                print("充值成功，您现在的余额为\033[31;1m{balance}\033[0m".format(balance=new_balance))
                                break
                            else:
                                print("\033[31;充值失败！\033[0m")
                        else:
                            print("\033[31;1m您输入的余额不合法，请重新输入！\033[0m")
            else:
                print("\033[31;1m您的选项不存在！\033[0m")
        elif choice == "b":
            break
        elif choice == "q":
            exit("Goodbye!")
        else:
            print("\033[31;1m您的选项不存在！\033[0m")

def shopping():
    balance = view_balance(balance_file=balance_file)
    shopping_info = []
    total_price = 0
    while True:
        goods_num = view_goods()
        choice = input("请选择您要购买的商品【1-{lenth}】: ".format(lenth=goods_num))
        if choice.isdigit():
            choice = int(choice)
            if choice <= goods_num:
                goods_info = linecache.getline(goods_file,choice)
                goods_name = goods_info.split(":")[0]
                goods_price = int(goods_info.split(":")[1].rstrip())
                total_price += goods_price
                shopping_info.append((goods_name, goods_price))
                choice = input("商品{goods_name}已加入购物车，是否继续购买【Y/N】:".format(goods_name=goods_name))
                if choice not in ["Y", "y"]:
                    choice = input("是否需要去删除不必要的商品【Y/N】: ")
                    if choice in ["Y", "y"]:
                        while True:
                            for index,item in enumerate(shopping_info):
                                print("{index} {item}".format(index=index+1,item=item))
                            choice = input("选择您要删除的商品编号[0-{length}]: ".format(length=len(shopping_info)))
                            if choice.isdigit():
                                choice = int(choice)
                                if choice <= len(shopping_info):
                                    index = choice - 1
                                    total_price -= shopping_info[index][1]
                                    del_goods_info = shopping_info.pop(index)
                                    choice = input("删除商品{del_goods_info}成功,是否继续删除不需要的商品【Y/N】".format(del_goods_info=del_goods_info))
                                    if choice not in ["Y", "y"]:
                                        break
                                else:
                                    choice = input("\033[31;1m您的选项不存在，是否继续删除不需要的商品【Y/N】\033[0m")
                                    if choice not in ["Y", "y"]:
                                        break
                            else:
                                choice = input("\033[31;1m您的选项不合法，是否继续删除不需要的商品【Y/N】\033[0m")
                                if choice not in ["Y", "y"]:
                                    break
                    while balance < total_price:
                        print("您的购物车：")
                        for index, item in enumerate(shopping_info):
                            print("{index} {item}".format(index=index + 1, item=item))
                        print("总金额：{total_price}".format(total_price=total_price))
                        choice = input("\033[31;1m您的余额{balance}不足 \033[0m需要选择删除购物车商品[1-{length}]: ".format(balance=balance,length=len(shopping_info)))
                        if choice.isdigit():
                            choice = int(choice)
                            if choice <= len(shopping_info):
                                index = choice - 1
                                total_price -= shopping_info[index][1]
                                del_goods_info = shopping_info.pop(index)
                                print("删除商品{del_goods_info}成功.".format(del_goods_info=del_goods_info))
                            else:
                                print("\033[31;1m您的选项不存在!\033[0m")
                        else:
                            print("\033[31;1m您的选项不合法!\033[0m")

                    f_a = open(shopping_file, "a", encoding="utf-8")
                    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    f_a.write(now_time + "\n")
                    for index,item in enumerate(shopping_info):
                        item_str = item[0] + ":" + str(item[1]) + "\n"
                        f_a.write(item_str)
                    f_a.close()
                    new_balance = balance - total_price
                    f_w = open(balance_file, "w", encoding="utf-8")
                    f_w.write(str(new_balance))
                    f_w.close()
                    print("购物成功！")
                    input("输入任意键继续： ")
                    break
            else:
                choice = input("您选择的商品不存在，是否继续购买【Y/N】:")
                if choice not in ["Y", "y"]:
                    break



def view_balance(balance_file="balance"):
    f_r = open(balance_file, "r", encoding="utf-8")
    balance = f_r.read()
    if balance.isdigit():
        balance = int(balance)
    else:
        balance = 0
    return balance
#######################

goods_file = "goods_info"
balance_file = "balance"
shopping_file = "shopping_info"
info = '''
请选择您的角色：
    【1】商场用户
    【2】消费者
    【q】退出系统
'''
while True:
    choice = input(info)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            manager()
        elif choice ==2:
            consumer()
        else:
            print("\033[31;1mInvalid option!\033[0m")
    elif choice == "q":
        exit("Goodbye!")
    else:
        print("\033[31;1mInvalid option!\033[0m")


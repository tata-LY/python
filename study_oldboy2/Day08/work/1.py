#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 10:26
# @Author  : liuyang
# @File    : 111.py
# @Software: PyCharm

import pickle

menu_file = 'menu'
with open(menu_file, "rb") as f_r:
    menu = f_r.read()
    if menu:
        menu = pickle.loads(menu)
    else:
        menu = {}

# print(type(menu), menu)


def print_error(data):
    print('\033[31;1m%s\033[0m' % data)


def choice(data):
    for index, val in enumerate(data):
        if data[index] != '返回':
            print('【%s】 %s' % (index+1, val))
        else:
            print('【b】 %s' % val)
    while True:
        your_choice = input("【q】 退出\n请选择>>>").strip()
        if your_choice == 'q':exit()
        if your_choice == 'b':your_choice = str(len(data))    # 选择your_choice=b时，把b转换为data列表最后一个下标（返回的下标）
        if your_choice in [str(index) for index in range(1, len(data)+1)]:
            return int(your_choice)
        else:
            print_error("错误的选项，重新选择!")

current_menu = menu
parrent_menu = []
level = 1

while True:
    if isinstance(current_menu, dict):
        data = [index for index in current_menu]
        if level != 1:data.append('返回')
        print('进入第%d级菜单'.center(30, "*") % level)
        your_choice = choice(data)
        if your_choice == len(data):
            if level ==1:
                break
            else:
                current_menu = parrent_menu.pop()  # parrent_menu最后一个值就是parrent_menu
                level -= 1
        else:
            parrent_menu.append(current_menu)     # 父级的字典追加到parrent_menu,当返回上一级时，列表最后一个值就是current的父字典。
            current_menu = current_menu[data[your_choice-1]]
            level += 1
    elif isinstance(current_menu, list):
        print('进入第%d级菜单'.center(30, "*") % level)
        print(current_menu)
        while True:
            your_choice = input("最后一层目录，b返回上一层目录>>>")
            if your_choice in ['b', 'B', 'back']:
                current_menu = parrent_menu.pop() # parrent_menu最后一个值就是parrent_menu
                level -= 1
                break
            else:
                print_error("错误的选项，重新选择!")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 10:30
# @Author  : liuyang
# @File    : 1_3level_menu.py
# @Software: PyCharm
import pickle

def get_menu(menu_file):
    with open(menu_file, "rb") as f_r:
        menu = f_r.read()
        if menu:
            menu = pickle.loads(menu)
        else:
            menu = {}
    return menu

def write_menu(menu_file, menu):
    with open(menu_file, "wb") as f_w:
        f_w.write(pickle.dumps(menu))

def print_error(data):
    print('\033[31;1m%s\033[0m' % data)

def choice(option):
    for index in option:
        print('【%s】 %s' % (index, option[index]))
    while True:
        your_choice = input("请选择>>>")
        if your_choice in str(option):
            return your_choice
        else:
            print_error("错误的选项，重新选择!")

menu_file = 'menu'
menu = get_menu(menu_file)
current_menu = menu
parrent_menu = [] # 里面元素存字典，key为选择的字，val为父级字典数据
level = 1

while True:
    if isinstance(current_menu, dict):
        option_data = {}
        count = 1
        for index in current_menu:
            option_data[count] = index
            count += 1
        if level != 1:
            option_data['b'] = '返回'
        option_data['q'] = '退出'

        print('进入第%d级菜单'.center(30, "*") % level)
        your_choice = choice(option_data)

        if your_choice == 'q':
            exit('退出程序')
        elif your_choice == 'b':
            if level ==1:
                break
            else:
                current_menu = parrent_menu.pop()  # parrent_menu最后一个值就是parrent_menu
                level -= 1
        else:
            option = option_data[int(your_choice)]
            parrent_menu.append(current_menu)     # 父级的字典追加到parrent_menu,当返回上一级时，列表最后一个值就是current的父字典。
            current_menu = current_menu[option]
            level += 1
    elif isinstance(current_menu, list):
        print('进入第%d级菜单'.center(30, "*") % level)
        print(current_menu)
        while True:
            your_choice = input("最后一层目录，b返回上一层目录>>>")
            if your_choice in ['b', 'B', 'back']:
                current_menu = parrent_menu.pop()  # parrent_menu最后一个值就是parrent_menu
                level -= 1
                break
            else:
                print_error("错误的选项，重新选择!")
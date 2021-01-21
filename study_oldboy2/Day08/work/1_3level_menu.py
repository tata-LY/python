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
    """

    :param option:
    :return: your_choice string
    """
    option_str = []
    for index in option:
        print('【%s】 %s' % (index, option[index]))
        option_str.append(str(index))
    while True:
        your_choice = input("请选择>>>")
        if your_choice in option_str:
            return your_choice
        else:
            print_error("错误的选项，重新选择!")

menu_file = 'menu'
menu = get_menu(menu_file)
current_menu = menu
parrent_menu = [] # parrent_menu里面存列表，列表第一个值是上一级选择的index，列表第二个值是上一级字典。比如[('湖南省', menu字典)]
level = 1

while True:
    if isinstance(current_menu, dict):
        option_data = {}
        count = 1
        for index in current_menu:
            option_data[count] = index
            count += 1
        option_data['a'] = '增加目录'
        if level != 1:
            option_data['b'] = '返回'
        option_data['q'] = '退出'

        print('进入第%d级目录'.center(30, "*") % level)
        your_choice = choice(option_data)

        if your_choice == 'a':
            add_menu_name = input('增加第%d级目录>>>' % level)
            if len(parrent_menu) == 0:
                menu[add_menu_name] = {}
            else:
                is_last_layer = input('是最后一层嘛[Y/N]>>>')
                for index in range(len(parrent_menu)-1, -1, -1):  # index倒序
                    option = parrent_menu[index][0]
                    if index == len(parrent_menu) -1 :
                        next_option = add_menu_name
                        if is_last_layer in ['Y', 'y']:
                            parrent_menu[index][1][option][next_option] = []
                        else:
                            parrent_menu[index][1][option][next_option] = {}
                    else:
                        next_option = parrent_menu[index+1][0]
                        parrent_menu[index][1][option][next_option] = parrent_menu[index+1][1]
            write_menu(menu_file, menu)
        elif your_choice == 'q':
            exit('退出程序')
        elif your_choice == 'b':
            if level ==1:
                break
            else:
                # current_menu = parrent_menu.pop()  # parrent_menu列表最后一个值就是parrent_menu
                current_menu = parrent_menu.pop()[1]  # parrent_menu列表最后一个列表的第二个值就是parrent_menu
                level -= 1
        else:
            option = option_data[int(your_choice)]
            # parrent_menu.append(current_menu)     # 父级的字典追加到parrent_menu,当返回上一级时，列表最后一个值就是current的父字典
            parrent_menu.append([option, current_menu])  # 把选择的项和current_menu增加到parrent_menu
            current_menu = current_menu[option]
            level += 1
    elif isinstance(current_menu, list):
        # print(parrent_menu)
        print('进入第%d级目录'.center(30, "*") % level)
        print(current_menu)
        while True:
            your_choice = input("最后一层目录，b返回上一层目录>>>")
            if your_choice in ['b', 'B', 'back']:
                # current_menu = parrent_menu.pop()  # parrent_menu列表最后一个值就是parrent_menu
                current_menu = parrent_menu.pop()[1]  # parrent_menu列表最后一个列表的第二个值就是parrent_menu
                level -= 1
                break
            else:
                print_error("错误的选项，重新选择!")
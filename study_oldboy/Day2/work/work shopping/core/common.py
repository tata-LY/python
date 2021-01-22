#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 10:59
# @Author  : liuyang
# @File    : common.py
# @Software: PyCharm

import os

def print_error(data):
    print('\033[31;1m%s\033[0m' % data)

def choice(option):
    """
    菜单选择
    :param option: 选项
    :return: your_choice
    """
    for index in option:
        print('【%s】 %s' % (index, option[index]))
    while True:
        your_choice = input("请选择>>>")
        if your_choice in option:
            return your_choice
        else:
            print_error("错误的选项，重新选择!")

def read_file(file_name):
    """
    读取file内容
    :param file_name: 文件名
    :return: result列表返回文件内容
    """
    result = []
    if os.path.isfile(file_name):
        f_r = open(file_name, 'r', encoding='utf-8')
        result = f_r.readlines()
        f_r.close()
    return result


def add_file(file_name, data):
    f_a = open(file_name, 'a', encoding='utf-8')
    f_a.write(data)
    f_a.close()

def write_file(file_name, data):
    f_w = open(file_name, 'w', encoding='utf-8')
    f_w.write(data)
    f_w.close()

def display(data):
    """
    展示列表信息
    :param data: 列表
    :return:
    """
    for _, val in enumerate(data):
        print(val, end='')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 10:57
# @Author  : liuyang
# @File    : manager.py
# @Software: PyCharm

from core import common
from conf import settings

def view_goods():
    """查看商品"""
    goods_file = settings.goods_file
    result = common.read_file(goods_file)
    if result:
        print('商品列表'.center(30, '*'))
        common.display(result)
    else:
        common.print_error('数据不存在！')
    input('输入回车键继续>>>')


def add_goods():
    """增加商品"""
    goods_file = settings.goods_file
    while True:
        good_name = input("商品名称>>>")
        while True:
            good_price = input("商品价格>>>")
            if good_price.isdigit():
                break
            else:
                common.print_error('商品价格不合法，请重新输入!')
        good_data = good_name + ' : ' + good_price + '\n'
        common.add_file(goods_file, good_data)
        print('%s添加成功！' % good_name)

        is_continue = input('继续添加商品[Y/y]>>>')
        if is_continue not in ['Y', 'y', 'yes']:
            break

def mod_goods():
    """修改商品价格"""
    goods_file = settings.goods_file
    goods_file = settings.goods_file
    goods_data = {}
    result = common.read_file(goods_file)
    if result:
        count = 1
        for _, val in enumerate(result):
            goods_data[str(count)] = val.rstrip()  # rstrip()删除右侧换行符
            count += 1
    else:
        common.print_error('无商品存在！')
    print('商品价格调整'.center(30, '*'))
    your_choice = common.choice(goods_data)
    while True:
        good_price = input("商品价格>>>")
        if good_price.isdigit():
            break
        else:
            common.print_error('商品价格不合法，请重新输入!')
    goods_data[your_choice] = goods_data[your_choice].split(':')[0] + ' : ' + good_price
    data = '' # str类型写入文件
    for index in goods_data:
        data += goods_data[index] + '\n'
    common.write_file(goods_file, data)
    print('%s修改成功！' % goods_data[your_choice])

    input('输入回车键继续>>>')

def del_goods():
    """删除商品"""
    goods_file = settings.goods_file
    goods_data = {}
    result = common.read_file(goods_file)
    if result:
        count = 1
        for _, val in enumerate(result):
            goods_data[str(count)] = val.rstrip() # rstrip()删除右侧换行符
            count += 1
    else:
        common.print_error('无商品存在！')
    print('商品下架'.center(30, '*'))
    your_choice = common.choice(goods_data)
    del_good_name = goods_data.pop(your_choice)
    data = '' # str类型写入文件
    for index in goods_data:
        data += goods_data[index] + '\n'
    common.write_file(goods_file, data)
    print('%s删除成功！' % del_good_name)

    input('输入回车键继续>>>')


def main():
    option = {
        'v': '查看商品',
        'a': '增加商品',
        'm': '修改商品',
        'd': '删除商品',
        'b': '返回',
        'q': '退出系统'
    }
    while True:
        choice = common.choice(option)
        if choice == 'v':
            view_goods()
        elif choice == 'a':
            add_goods()
        elif choice == 'm':
            mod_goods()
        elif choice == 'd':
            del_goods()
        elif choice == 'b':
            break
        elif choice == 'q':
            exit("欢迎下次光临！")


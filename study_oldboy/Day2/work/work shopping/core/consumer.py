#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 10:57
# @Author  : liuyang
# @File    : consumer.py
# @Software: PyCharm

from core import common
from conf import settings


def view_balance():
    balance_file = settings.balance_file
    data = common.read_file(balance_file)
    if len(data) == 1 and data[0].isdigit():
        print('余额：￥%s' % data[0])
    else:
        common.print_error("余额异常！")
    input('输入回车键继续>>>')

def balance_recharge():
    balance_file = settings.balance_file
    data = common.read_file(balance_file)
    if len(data) == 1 and data[0].isdigit():
        print('余额：￥%s' % data[0])
        while True:
            recharge = input('充值金额>>>')
            if recharge.isdigit():
                break
            else:
                common.print_error("充值金额有误！")
        now_balance = str(int(data[0]) + int(recharge))
        common.write_file(balance_file, now_balance)
        print("充值成功，当前余额为￥%s" % now_balance)
    else:
        common.print_error("余额异常！")
    input('输入回车键继续>>>')

def shopping():
    goods_file = settings.goods_file
    balance_file = settings.balance_file
    goods_data = {}
    goods_cart = []
    result = common.read_file(goods_file) # list
    if result:
        count = 1
        for _, val in enumerate(result):
            goods_data[str(count)] = val.rstrip()  # rstrip()删除右侧换行符
            count += 1
    else:
        common.print_error('无商品存在！')
    print('购物中'.center(30, '*'))
    while True:
        your_choice = common.choice(goods_data)
        goods_cart.append(goods_data[your_choice])
        is_continue = input('是否继续添加商品到购物车[Y/y]>>>')
        if is_continue not in ['Y', 'y', 'yes']:
            break

    print('购物车：%s' % goods_cart)
    is_pay = input('付款[Y/y]>>>')
    if is_pay in ['Y', 'y', 'yes']:
        total = 0
        for _, val in enumerate(goods_cart):
            total += int(val.split(':')[1].lstrip())
        now_balance = int(common.read_file(balance_file)[0])
        if now_balance >= total:
            common.write_file(balance_file, now_balance)
            print("购物成功，当前余额为￥%s" % now_balance)
        else:
            common.print_error('商品总金额为%d,卡内余额%d,请充值！' % (total, now_balance))
    else:
        common.print_error('付款失败，购物结束！ ')
    input('输入回车键继续>>>')


def main():
    option = {
        '1': '购买商品',
        '2': '查看余额',
        '3': '余额充值',
        'b': '返回',
        'q': '退出系统'
    }
    while True:
        choice = common.choice(option)
        if choice == '1':
            shopping()
        elif choice == '2':
            view_balance()
        elif choice == '3':
            balance_recharge()
        elif choice == 'b':
            break
        elif choice == 'q':
            exit("欢迎下次光临！")
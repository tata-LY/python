#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from core import db_handler


def credit_card_pay(account_id, password, pay_money):
    user_data = db_handler.db_select(account_id, password)
    pay_money = float(pay_money)
    if user_data:
        amount = user_data['amount']
        credit = user_data['credit']
        if credit - pay_money + amount < 0:
            print("Exceeded credit card limit.")
            return False
    else:
        print("login is failed!")
        return False
    new_credit = credit - pay_money
    user_data['credit'] = new_credit
    if db_handler.db_update(user_data):
        return True
    else:
        return False

def bank_card_pay(account_id, password, pay_money):
    user_data = db_handler.db_select(account_id, password,)
    pay_money = float(pay_money)
    if user_data:
        balance = user_data['balance']
        if pay_money > balance:
            print("Insufficient balance.")
            return False
    else:
        print("login is failed!")
        return False
    new_balance = balance - pay_money
    user_data['balance'] = new_balance
    if db_handler.db_update(user_data):
        return True
    else:
        return False
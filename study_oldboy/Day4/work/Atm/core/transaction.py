#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
from core import db_handler

def transaction(transaction_type, amount, user_data, **others):
    action = settings.TRANSACTION_TYPE[transaction_type]['action']
    interest = settings.TRANSACTION_TYPE[transaction_type]['interest']
    amount = float(amount)
    balance = float(user_data['balance'])
    credit = float(user_data['credit'])
    if action == 'plus':
        new_balance = balance + amount + amount * interest
    elif action == 'minus':
        if balance < amount:
            return
        new_balance = balance - amount - amount*interest

    user_data['balance'] = new_balance
    if transaction_type == "repay":
        new_credit = credit + amount
        user_data['credit'] = new_credit
    print(user_data)
    return user_data
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys
from core import logger
from core import auth
from core.auth import login_required
from core import db_handler
from core import transaction

user_info = {
   'account_id': None,
   'is_auth': False,
   'account_data': None,
}

@login_required
def account_info(user_info):
   account_data = user_info['account_data']
   print("\033[35;1mAccount [{user}] info :\033[0m".format(user = account_data['id']))
   for key,value in account_data.items():
      print("{key} : {value}".format(key=key, value=value))
   logger.logger('atm', 'User[{user}] view personal information.'.format(user = account_data['id']))
   input("Enter any key to continue： ")
   return user_info

@login_required
def  repay(user_info):
   user_data = user_info['account_data']
   print("--- Acccount Repayment ---")
   amount = input("Repayment amount: ")
   if amount.isdigit():
      user_data = transaction.transaction('repay', amount, user_data)
      if user_data:
         user_info['account_data'] = user_data
         db_handler.db_update(user_data)
         print("User {user} repay ${money} successfully.".format(user=user_data['id'],money=amount))
         logger.logger('atm', "User {user} repay ${money} successfully.".format(user=user_data['id'],money=amount))
      else:
         print("\033[31;1mRepayment failed.\033[0m")
   else:
      print("\033[31;1mRepayment failed.\033[0m")
   return user_info

@login_required
def withdraw(user_info):
   user_data = user_info['account_data']
   print("--- Acccount Withdraw ---")
   amount = input("Withdraw amount: ")
   if amount.isdigit():
      user_data = transaction.transaction('withdraw', amount, user_data)
      if user_data:
         user_info['account_data'] = user_data
         db_handler.db_update(user_data)
         print("User {user} withdraw ${money} successfully.".format(user=user_data['id'],money=amount))
         logger.logger('atm', "User {user} withdraw ${money} successfully.".format(user=user_data['id'],money=amount))
      else:
         print("\033[31;1mwithdraw failed.\033[0m")
   else:
      print("\033[31;1mwithdraw failed.\033[0m")
   return user_info

@login_required
def transfer(user_info):
   user_data = user_info['account_data']
   print('Account transfer'.center(50, '-'))
   other_account =  input('Other account id>>>').strip()
   other_account_data = db_handler.db_select(other_account, '', transfer = 'transfer')   # 转账时增加transfer标识，在db处理的时候不需要验证密码。
   if other_account == user_data['id'] or not other_account_data:
      print("\033[31;1mTransfer amount failed.\033[0m")
      return user_info
   transfer_amount = input('Transfer amount>>>').strip()
   if not transfer_amount.isdigit():
      print("\033[31;1mTransfer amount failed.\033[0m")
      return user_info
   else:
      transfer_amount = int(transfer_amount)
   if user_data['balance'] < transfer_amount:
      print("\033[31;1mSorry, your credit is running low.\033[0m")
      return user_info
   user_data['balance'] -= transfer_amount
   other_account_data['balance'] += transfer_amount
   db_handler.db_update(user_data)
   db_handler.db_update(other_account_data)
   print("User %s Transter %d to %s successfully." % (user_data['id'], transfer_amount, other_account))
   logger.logger('atm', "User %s Transter %d to %s successfully." % (user_data['id'], transfer_amount, other_account))
   return user_info

@login_required
def account_bill(user_info):
   return user_info

@login_required
def save_money(user_info):
   print("--- Save money ---")
   user_data = user_info['account_data']
   money = input("Deposit card amount: ")
   if money.isdigit():
      money = int(money)
      user_data = transaction.transaction('save_money', money, user_data)
      if user_data:
         user_info['account_data'] = user_data
         db_handler.db_update(user_data)
         print("User {user} saved ${money} successfully.".format(user=user_data['id'],money=money))
         logger.logger('atm', "User {user} saved ${money} successfully.".format(user=user_data['id'],money=money))
      else:
         print("\033[31;1mSave money failed.\033[0m")
   else:
      print("\033[31;1mSave money failed.\033[0m")
   return user_info

def logout(user_info):
   user_info['is_auth'] = False
   logger.logger('access', "User [{user}] exit ZJLY bank atm system.".format(user=user_info['account_data']['id']))
   return user_info

def interactive(user_info):
   menu = u'''
------- Welcome user [{user}] login ZJLY Bank system ---------
1. View account information（查看余额）
2. Account repayment（还款）
3. Account withdrawal（取现）
4. Account transfer to other account（转账）
5. View account bill（查看账单）(no do)
6. Save money（存钱）
7. logout'''.format(user=user_info['account_data']['id'])
   menu_dic = {
      '1': account_info,
      '2': repay,
      '3': withdraw,
      '4': transfer,
      '5': account_bill,
      '6': save_money,
      '7': logout,
   }
   while user_info['is_auth']:
      print(menu)
      user_option = input("Your choice>>>:").strip()
      if user_option in menu_dic:
         print('user_info: ', user_info)
         user_info = menu_dic[user_option](user_info)
      else:
         print("\033[31;1mOption does not exist!\033[0m")

def run():
   while True:
      user_info = auth.main()
      # user_info = {'is_auth': True,
      #                 'account_data': {'id': 'ly', 'password': '123456', 'expire_date': '2021-01-01', 'balance': 10000,
      #                                  'amount': 30000, 'credit': 0, 'status': 0}}
      interactive(user_info)
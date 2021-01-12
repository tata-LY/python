#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
from core import logger
from core import db_handler
import os
import sys
import json

def login_required(func):
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        if args[0]['is_auth']:
            res = func(*args, **kwargs)
            return res
        else:
            exit("User is not authenticated.")
    return wrapper


def account_apply():
    print("--- Account Application ---")
    account = input("account: ").strip()
    password = input("passwd: ").strip()
    account_info = {
        'id': account,
        'password': password,
        'expire_date': '2021-01-01',
        'balance': 0,
        'amount': 30000,
        'credit': 0,
        'status': 0, # 0 = normal, 1 = locked, 2 = disabled
    }
    # db_path = db_handler.db_handler()
    # account_file = "%s/%s.json" % (db_path, account)
    res = db_handler.db_add(account_info)
    if res:
        print("\033[32;1mAtm account application is successful.\033[0m")
        logger.logger('atm', "Atm account [{id}] application is successful.".format(id=account))
    else:
        print("\033[31;1mAccount is existed.\033[0m")
        logger.logger('atm', "Atm account [{id}] application is failed, account is existed.".format(id=account))

# def account_auth(account, password):
#     db_path = db_handler.db_handler()
#     account_file = "%s/%s.json" % (db_path, account)
#     if os.path.exists(account_file):
#         with open(account_file, "r", encoding="utf-8") as f_r:
#             account_data = json.loads(f_r.read())
#             if account_data['password'] == password:
#                 return account_data

def account_login():
    retry_count = 0
    user_info = {}
    user_info['is_auth'] = False
    while retry_count < 3 and user_info['is_auth'] is not True:
        print("--- Account Login ---")
        account = input("account: ").strip()
        password = input("passwd: ").strip()

        # user_data = account_auth(account, password)
        user_data = db_handler.db_select(account, password)
        if user_data:
            user_info['account_id'] = user_data['id']
            user_info['account_data'] = user_data
            user_info['is_auth'] = True
            logger.logger('access', "User [{account}] login ZJLY bank atm system succeeded.".format(account=account))
            return user_info
        else:
            retry_count += 1
            print("\033[31;1mUser password is incorrect,hava {count} times chances to try\033[0m".format(count=3-retry_count))
    else:
        print("\033[31;1mIncorrect account or password tried three times!\033[0m")

def main():
    while True:
        info = '''---Welcome to ZJLY Bank system ---
    1. account login
    2. account application
    b. exit system'''
        choice_dict = {
            '2': account_apply,
            '1': account_login,
        }
        print(info)
        choice = input("Your choice>>>")
        if choice in choice_dict:
            user_info = choice_dict[choice]()
            if user_info :
                return user_info
        elif choice == 'b':
            exit("Goodbye!")
        else:
            print("\033[31;1mOption is not exist!\033[0m")
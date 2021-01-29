#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
from core import logger
import os
import sys
import json

def login_required(func):
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        if args[0]:     # is_auth=True
            res = func(*args, **kwargs)
            return res
        else:
            exit("User is not authenticated.")
    return wrapper

def account_login(user_type):
    """登录"""
    user_file = "%s/accounts/%s" % (settings.DATABASE['path'], settings.USER_TYPES[user_type])  # 根据user_type拼接数据库文件绝的路径
    password = input("请输入[%s]口令：" % settings.USER_TYPES[user_type])
    if os.path.exists(user_file):
        with open(user_file, "r", encoding="utf") as f_r:
            if password == f_r.read():
                return True
            else:
                return False
    else:
        return False
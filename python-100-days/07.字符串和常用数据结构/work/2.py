#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-8 15:11
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm
"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random
import string

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    code = ''
    all_char = string.digits + string.ascii_letters # 0-9数字 + 26个大小写字母
    all_char_len = len(all_char)
    for _ in range(0, code_len):
        code += all_char[random.randint(0, all_char_len-1)]   # all_char随机下标
    return code
if __name__ == '__main__':
    print(generate_code(6))
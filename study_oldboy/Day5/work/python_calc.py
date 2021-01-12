#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import re

def check(string):
    flag = True
    string = string.replace(" ", "")
    # 判断算术表达式是不是合法
    res = re.match("[\d\(\)\+\-\*\/\.]*", string).group()
    if res == string:
        return string
    else:
        exit("输入的表达式不合法")

def format_string(string):
    string = string.replace('--', '+')
    string = string.replace('-+', '-')
    string = string.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace('+*', '*')
    string = string.replace('+/', '/')
    return string

def mul_div(expression):
    flag = True
    while flag:
        pattern = "[\d\.]+[\*\/]\-{0,1}[\d\.]+"
        strs = re.findall(pattern, expression)
        if strs:
            for s in strs:
                if re.search("\*", s):
                    x, y = s.split("*")
                    new_s = float(x) * float(y)
                    expression = expression.replace(s, str(new_s))
                else:
                    x, y = s.split("/")
                    new_s = float(x) / float(y)
                    expression = expression.replace(s, str(new_s))
        else:
            flag = False
            return format_string(expression)

def add_sub(expression):
    flag = True
    while flag:
        pattern = "[\d\.]+[\-\+][\d\.]+"
        strs = re.findall(pattern, expression)
        if strs:
            for s in strs:
                if re.search("\+", s):
                    x, y = s.split("+")
                    new_s = float(x) + float(y)
                    expression = expression.replace(s, str(new_s))
                else:
                    x, y = s.split("-")
                    new_s = float(x) - float(y)
                    expression = expression.replace(s, str(new_s))
        else:
            flag = False
            return format_string(expression)

if __name__ == '__main__':
    expression = input('请输入要计算的表达式: ')
    expression = check(expression)
    expression = format_string(expression)
    print('表达式:', expression)
    while expression.count('(') > 0:
        strs = re.findall("\([\d\+\-\*\/\.]+\)", expression)
        for expr in strs:
            new_expr = mul_div(expr)
            new_expr = add_sub(new_expr)
            new_expr = new_expr.replace("(", "")
            new_expr = new_expr.replace(")", "")
            expression = format_string(expression.replace(expr, new_expr))
    else:
        expression = format_string(mul_div(expression))
        expression = add_sub(expression)
    print("计算结果：",expression)

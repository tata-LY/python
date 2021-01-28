#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import re

def check(string):
    """
    判断表达式是否合法
    1.只包含数字+-*/.符号
    2.括号个数是否正常'（'个数='）'个数
    """
    flag = True
    string = string.replace(" ", "")
    # 判断算术表达式是不是合法
    res = re.match("[\d\(\)\+\-\*\/\.]*", string).group()
    if res != string:flag = False
    # 检查括号是不是一一对应
    res1 = re.findall('\(', string)
    res2 = re.findall('\)', string)
    if len(res1) != len(res2):flag = False
    if flag:
        return string
    else:
        exit("输入的表达式不合法!")

def format_string(string):
    """
    格式化加减乘除
    """
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
    """
    接收没有括号的表达式，处理所有的乘除
    :expression  没有括号的表达式
    :return 处理乘除后格式化的结果
    """
    flag = True
    while flag:
        pattern = "[\d\.]+[\*\/]\-{0,1}[\d\.]+"
        strs = re.findall(pattern, expression)      # 找出所有*/乘除的表达式，比如1*2,3/5
        if strs:
            for s in strs:
                if re.search("\*", s):  # 处理*乘法
                    x, y = s.split("*")
                    new_s = float(x) * float(y)
                    expression = expression.replace(s, str(new_s))
                else:
                    x, y = s.split("/") # 处理/除法
                    new_s = float(x) / float(y)
                    expression = expression.replace(s, str(new_s))  # 用乘除结果直接替换匹配的表达式
        else:
            flag = False    # 无*/就退出
            return format_string(expression)

def add_sub(expression):
    """
    接收没有括号的表达式，处理所有的加减
    :expression  没有括号的表达式
    :return 处理加减后格式化的结果
    """
    flag = True
    while flag:
        pattern = "[\d\.]+[\-\+][\d\.]+"
        strs = re.findall(pattern, expression)  # 找出所有-+加减的表达式，比如1+2,3-5
        if strs:
            for s in strs:
                if re.search("\+", s):  # 处理+
                    x, y = s.split("+")
                    new_s = float(x) + float(y)
                    expression = expression.replace(s, str(new_s))
                else:
                    x, y = s.split("-") # 处理-
                    new_s = float(x) - float(y)
                    expression = expression.replace(s, str(new_s))  # 用乘除结果直接替换匹配的表达式
        else:
            flag = False    # 无+-就退出
            return format_string(expression)

if __name__ == '__main__':
    expression = input('请输入要计算的表达式: ')
    expression = check(expression)
    expression = format_string(expression)
    print('表达式:', expression)
    while expression.count('(') > 0:
        strs = re.findall("\([\d\+\-\*\/\.]+\)", expression)    # 找出表达式最深一层的(*)
        print(strs)
        for expr in strs:
            new_expr = mul_div(expr)    # 算乘除
            new_expr = add_sub(new_expr)    # 算加减
            new_expr = new_expr.replace("(", "")    # 得出的结果去掉'('
            new_expr = new_expr.replace(")", "")    # 得出的结果去掉')'
            expression = format_string(expression.replace(expr, new_expr))  # 用加减乘除算出来的值替换之前的表达式，赋值给expression，循环处理，直到没有括号。
    else:
        expression = format_string(mul_div(expression))
        expression = add_sub(expression)
    print("计算结果：",expression)

"""
测试用例：1 - 2 * ( (60.3-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
第一轮结果：
['(-40/5)', '(9-2*5/3+7/3*99/4*2998+10*568/14)', '(-4*3)', '(16-3*2)']
(-8.0)
(-8.0)
-8.0)
-8.0
1-2*((60-30-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
"""
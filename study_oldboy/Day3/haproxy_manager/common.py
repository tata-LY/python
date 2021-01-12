#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import re

def print_colour(data, type_num):
    data = data
    type_num = type_num
    print("\033[{type_num};1m{data}\033[0m".format(data=data,   type_num=type_num))

def option_choice(title="", option_list=[]):
    while True:
        print(title)
        for index, item in enumerate(option_list):
            if item == "b":
                item = "返回上一级"
            elif item == "q":
                item = "退出程序"
            print("{index}. {item}".format(index=index+1, item=item))
        choice = input("请输入您的选择: ")
        if choice.isdigit():
            choice = int(choice)
            if choice >=1 and choice <=len(option_list):
                if option_list[choice-1] == "q":
                    exit("Goodbye")
                # elif option_list[choice-1] == "b":
                #     return choice
                #     break
                else:
                    return choice
                    break
            else:
                print_colour("您输入的选项不存在,请重新选择", 31)
        else:
            print_colour("您输入的选项不存在,请重新选择", 31)

def isIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False

def get_used_ports(haproxy_config_file="haproxy.cfg"):
    used_ports = []
    with open(haproxy_config_file, "r", encoding="utf-8") as f_r:
        for line in f_r:
            if line.strip().startswith("bind"):
                port = line.strip().split(":")[-1]
                used_ports.append(port)
    return used_ports

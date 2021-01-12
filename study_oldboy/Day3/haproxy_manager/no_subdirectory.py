#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import common

all_proxy_mode = ["http", "tcp"]
all_proxy_balance = ["roundrobin", "leastconn", "cookie"]

def search(proxy_name, haproxy_config_file="haproxy.cfg"):
    proxy_name = proxy_name
    search_flag = False
    proxy_config = ""
    f_r = open(haproxy_config_file, "r", encoding="utf-8")
    for line in f_r:
        if line.strip().startswith("listen"):
            if line.strip().split()[1] == proxy_name:
                search_flag = True
            else:
                search_flag = False
        elif line.strip().startswith("backend") or line.strip().startswith("frontend "):
            search_flag = False
        elif line == "\n":
            search_flag = False
        if search_flag:
            proxy_config += line
    f_r.close()
    return proxy_config


def make_proxy_conf(proxy_name, proxy_port, proxy_mode, proxy_balance, server={}):
    proxy_conf1 = """
listen {proxy_name}
\tbind 0.0.0.0:{proxy_port}
\tmode {proxy_mode}
\tbalance {proxy_balance}
"""
    cookie_proxy_conf1 ="""
listen {proxy_name}
\tbind 0.0.0.0:{proxy_port}
\tmode {proxy_mode}
\tbalance {proxy_balance}
\tcookie {proxy_name} insert postonly
"""
    proxy_conf2 ="\tserver {proxy_name}_node{num} {server_ip}:{server_port} minconn 4 maxconn 10000 check inter 2000 rise 2 fall 5\n"
    cookie_proxy_conf2 ="\tserver {proxy_name}_node{num} {server_ip}:{server_port} cookie {proxy_name}_node{num} minconn 4 maxconn 10000 check inter 2000 rise 2 fall 5\n"
    proxy_conf = ""
    if proxy_balance == "cookie":
        proxy_conf1 = cookie_proxy_conf1
        proxy_conf2 = cookie_proxy_conf2

    proxy_conf += proxy_conf1.format(proxy_name=proxy_name, proxy_port=proxy_port, proxy_mode=proxy_mode, proxy_balance=proxy_balance)
    count = 0
    for key,value in server.items():
        count += 1
        proxy_conf += proxy_conf2.format(proxy_name=proxy_name, num=count, server_ip=key, server_port=value)
    return proxy_conf


def get_proxy_value(proxy_conf):
    proxy_conf = proxy_conf
    proxy_conf_dict = {}
    server = {}
    for line in proxy_conf.split("\n"):
        if line.strip().startswith("listen"):
            proxy_conf_dict["proxy_name"] = line.split()[1]
        if line.strip().startswith("bind"):
            proxy_conf_dict["proxy_port"] = line.split()[1]
        if line.strip().startswith("mode"):
            proxy_conf_dict["proxy_mode"] = line.split()[1]
        if line.strip().startswith("balance"):
            proxy_conf_dict["proxy_balance"] = line.split()[1]
        if line.strip().startswith("server"):
            server_ip = line.split(":")[0].split()[-1]
            server_port = line.split(":")[-1].split()[0]
            server[server_ip] = server_port
            proxy_conf_dict["server"] = server
    return proxy_conf_dict

def update(proxy_conf_dict):
    proxy_name = proxy_conf_dict["proxy_name"]
    proxy_port = proxy_conf_dict["proxy_port"]
    proxy_mode = proxy_conf_dict["proxy_mode"]
    proxy_balance = proxy_conf_dict["proxy_balance"]
    server = proxy_conf_dict["server"]

    choice = input("是否需要修改{proxy_name} Proxy端口【Y/N】: ".format(proxy_name=proxy_name))
    if choice in ["Y", "y"]:
        while True:
            used_ports = common.get_used_ports(haproxy_config_file="haproxy.cfg")
            proxy_port = input("请输入新的{proxy_name} Proxy代理端口[0-65535]：".format(proxy_name=proxy_name))
            if proxy_port.isdigit():
                if int(proxy_port) > 0 and int(proxy_port) < 65536:
                    if proxy_port in used_ports:
                        common.print_colour("您输入的端口{proxy_port}已被使用，请重新输入".format(proxy_port=proxy_port), 31)
                    else:
                        break
                else:
                    common.print_colour("您输入的端口不合法，端口范围为1-65535，请重新输入".format(proxy_name=proxy_name), 31)
            else:
                common.print_colour("您输入的端口不合法，端口范围为1-65535，请重新输入".format(proxy_name=proxy_name), 31)
    choice = input("是否需要修改{proxy_name} Proxy Mode【Y/N】: ".format(proxy_name=proxy_name))
    if choice in ["Y", "y"]:
        choice = common.option_choice("请选择以下Haproxy mode：", all_proxy_mode)
        proxy_mode = all_proxy_mode[choice - 1]

    choice = input("是否需要修改{proxy_name} Proxy Balance【Y/N】: ".format(proxy_name=proxy_name))
    if choice in ["Y", "y"]:
        choice = common.option_choice("请选择以下Haproxy Balance：", all_proxy_balance)
        proxy_balance = all_proxy_balance[choice - 1]

    choice = input("是否需要修改{proxy_name} Proxy server后端【Y/N】: ".format(proxy_name=proxy_name))
    if choice in ["Y", "y"]:
        server = {}
        count = 0
        while True:
            count += 1
            while True:
                server_ip = input("请输入第{count}个新增加的Haproxy Proxy后端服务IP[例如：172.25.2.1]：".format(count=count))
                if common.isIP(server_ip):
                    break
                else:
                    common.print_colour("您输入的IP不合法，请重新输入".format(proxy_name=proxy_name), 31)
            while True:
                server_port = input("请输入第{count}个新增加的Haproxy Proxy后端服务端口[1-65535]：".format(count=count))
                if int(server_port) >= 1 and int(server_port) <= 65535:
                    break
                else:
                    common.print_colour("您输入的端口不合法，请重新输入".format(proxy_name=proxy_name), 31)
            server[server_ip] = server_port
            choice = input("是否继续输入下一个Haproxy Proxy后端服务信息【Y/N】: ")
            if choice not in ["Y", "y", "yes", "YES"]:
                break
    return proxy_name, proxy_port, proxy_mode, proxy_balance , server

def delete(del_proxy_name,haproxy_conf_file="haproxy.cfg"):
    new_proxy_conf = ""
    del_flag = True
    with open(haproxy_conf_file, "r", encoding="utf-8") as f_r:
        for line in f_r:
            if line.strip().startswith("listen"):
                if line.strip().split()[1] == del_proxy_name:
                    del_flag = False
                else:
                    del_flag = True
            if line.strip().startswith("frontend") or line.strip().startswith("backend"):
                del_flag = True
            if del_flag:
                new_proxy_conf += line
    with open(haproxy_conf_file, "w", encoding="utf-8") as f_w:
        f_w.write(new_proxy_conf)
def show_app(haproxy_config_file="haproxy.cfg"):
    proxy_name_list = []
    f_r = open(haproxy_config_file, "r", encoding="utf-8")
    for line in f_r:
        if line.strip().startswith("listen"):
            proxy_name = line.split()[1]
            if proxy_name != "admin_stats":
                proxy_name_list.append(proxy_name)
    f_r.close()
    return proxy_name_list
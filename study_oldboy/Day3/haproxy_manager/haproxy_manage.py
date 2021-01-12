#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import common, no_subdirectory

haproxy_conf_file = "haproxy.cfg"
all_proxy_mode = ["http", "tcp"]
all_proxy_balance = ["roundrobin", "leastconn", "cookie"]

while True:
    option1 = ["非子目录配置管理", "子目录配置管理", "q"]
    choice = common.option_choice(option_list=option1, title="###########欢迎来到Haproxy配置管理程序###########")
    if choice == 1:
        while True:
            option2 = ["查看", "新增", "修改", "删除", "b", "q"]
            choice = common.option_choice(title="非子目录配置管理:", option_list=option2)
            if choice == 1:
                proxy_name_list = no_subdirectory.show_app(haproxy_config_file="haproxy.cfg")
                choice = common.option_choice("查看目前存在的非子目录配置：", proxy_name_list)
                proxy_name = proxy_name_list[choice-1]
                proxy_conf = no_subdirectory.search(proxy_name)
                print("{proxy_name}Haproxy proxy配置信息如下：\n{proxy_conf}".format(proxy_name=proxy_name, proxy_conf=proxy_conf))
                input("输入任意键继续： ")
            elif choice == 2:
                proxy_name = ""
                proxy_port = ""
                proxy_mode = ""
                proxy_balance = ""
                server = {}

                proxy_name_list = no_subdirectory.show_app(haproxy_config_file="haproxy.cfg")
                while True:
                    proxy_name = input("请输入新增加的Haproxy Proxy名字： ")
                    if proxy_name in  proxy_name_list:
                        common.print_colour("{proxy_name}已经存在，请重新输入".format(proxy_name=proxy_name), 31)
                    else:
                        break
                while True:
                    used_ports = common.get_used_ports(haproxy_config_file="haproxy.cfg")
                    proxy_port = input("请输入新增加的Haproxy Proxy代理端口[0-65535]：")
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

                choice = common.option_choice("请选择以下Haproxy mode：", all_proxy_mode)
                proxy_mode = all_proxy_mode[choice-1]

                choice = common.option_choice("请选择以下Haproxy Balance：", all_proxy_balance)
                proxy_balance = all_proxy_balance[choice-1]

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
                proxy_conf = no_subdirectory.make_proxy_conf(proxy_name, proxy_port, proxy_mode, proxy_balance, server)
                with open(haproxy_conf_file, "a", encoding="utf-8") as f_a:
                    f_a.write(proxy_conf)
                print("{proxy_name}添加成功，信息如下：\n{proxy_conf}".format(proxy_name=proxy_name, proxy_conf=proxy_conf))
                input("输入任意键继续：")
            elif choice == 3:
                proxy_name_list = no_subdirectory.show_app(haproxy_conf_file)
                choice = common.option_choice("以下Haproxy proxy配置可以修改：", proxy_name_list)
                update_proxy_name = proxy_name_list[choice-1]
                proxy_conf = no_subdirectory.search(update_proxy_name)
                print("{proxy_name} Proxy 配置信息如下：\n{proxy_conf}".format(proxy_name=update_proxy_name, proxy_conf=proxy_conf))
                proxy_conf_dict = no_subdirectory.get_proxy_value(proxy_conf)
                no_subdirectory.delete(update_proxy_name)
                proxy_name, proxy_port, proxy_mode, proxy_balance, server = no_subdirectory.update(proxy_conf_dict)
                new_proxy_conf = no_subdirectory.make_proxy_conf(proxy_name, proxy_port, proxy_mode, proxy_balance, server)
                with open(haproxy_conf_file, "a", encoding="utf-8") as f_a:
                    f_a.write(new_proxy_conf)
                print("{proxy_name}修改成功，信息如下：\n{proxy_conf}".format(proxy_name=update_proxy_name, proxy_conf=new_proxy_conf))
                input("输入任意键继续：")
            elif choice == 4:
                proxy_name_list = no_subdirectory.show_app(haproxy_conf_file)
                choice = common.option_choice("以下Haproxy proxy配置可以删除：", proxy_name_list)
                del_proxy_name = proxy_name_list[choice-1]
                no_subdirectory.delete(del_proxy_name,haproxy_conf_file)
                input("{proxy_name}配置已经删除，输入任意键继续： ".format(proxy_name=del_proxy_name))
            elif choice == 5:
                break
    elif choice == 2:
        print("2")
    elif choice == 3:
        exit("Goodbye!")
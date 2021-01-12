#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import re
import json

dirpath = "apps"  # 指定根目录

def error_log(data):
    data = data + "\n"
    error_file = "error_log.log"
    if not os.path.exists(error_file):
        with open(error_file, "w", encoding="utf-8") as f_w:
            f_w.write(data)
    else:
        with open(error_file, "a", encoding="utf-8") as f_a:
            f_a.write(data)

def get_config_files(dirname):
    config_files = []
    file_pattern = "properties$|xml$"
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if re.search(file_pattern, apath):
                config_files.append(apath)
    return config_files

def mod_app_config(data):
    pattern = "https{0,1}\\\\{0,1}\:\/\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\\\{0,1}\:\d+\/[\w-]+" # ['172.25.2.53\:50028/fpt-verifycode', '172.25.2.54:28004/dzht-zh']
    app_conf = re.findall(pattern, data)
    if app_conf:
        with open("conf.json", "r", encoding="utf-8") as f_r:
            conf_dict = json.loads(f_r.read())
        print("\033[31;1m配置文件{file}修改app配置:\033[0m".format(file=file))
        print(app_conf)
        for item in app_conf:
            name = re.search("\/[\w\-]*$", item).group().split("/")[1]  # 获取配置里的工程名
            protocol = re.search("^\w*", item).group()    # 获取配置的协议http or https
            flag = False
            if name in conf_dict:
                if conf_dict[name]['domain_name'] and conf_dict[name][protocol+"_port"]:
                    flag = True
            if flag:
                name = name
                protocol = protocol
                domain_name = conf_dict[name]['domain_name']
                port = conf_dict[name][protocol+"_port"]
                new_url = protocol + "://" + domain_name + ":" + port + "/" + name
                pattern = "https{0,1}\\\\{0,1}\:\/\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\\\{0,1}\:\d+\/" + name
                data = re.sub(pattern, new_url, data, count=1)   # 替换配置文件所有app配置的url
            else:
                print("\033[31;1m{name} 在列表中配置有问题，请检查。\033[0m".format(name=name))
                error_log("{name} 在列表中配置有问题，请检查。".format(name=name))
    return data

def mod_redis_config(data):
    # pattern = "\=192\.168\.71\.185"
    pattern = "cache.ip\=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    app_conf = re.findall(pattern, data)
    if app_conf:
        print("\033[31;1m配置文件{file}修改redis配置:\033[0m".format(file=file))
        print(app_conf)
        with open("conf.json", "r", encoding="utf-8") as f_r:
            conf_dict = json.loads(f_r.read())
            redis_domain_name = conf_dict['redis']['domain_name']
        for item in app_conf:
            new_redis_conf = item.split("=")[0] + '=' + redis_domain_name
            data = re.sub(pattern, new_redis_conf, data, count=1)
        # print(data)
    return data

def mod_rocketmq_config(data):
    pattern = "192\.168\.71\.35\\\\{0,2}\:9876"
    # pattern = "cache.ip\=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    app_conf = re.findall(pattern, data)
    if app_conf:
        print("\033[31;1m配置文件{file}修改redis配置:\033[0m".format(file=file))
        print(app_conf)
        with open("conf.json", "r", encoding="utf-8") as f_r:
            conf_dict = json.loads(f_r.read())
            rocketmq_url = conf_dict['rocketmq']['domain_name'] + ":" + conf_dict['rocketmq']['http_port']
        data = re.sub(pattern, rocketmq_url, data)
    return data

def other_config(data):
    # Hbase
    pattern = ".*\=192.168.71.194,192.168.71.196,196.168.71.198"
    app_conf = re.findall(pattern, data)
    if app_conf:
        print("\033[31;1m配置文件{file} 有Hbase配置:\033[0m\033[0m".format(file=file))
        print(app_conf)

    # Oracle
    pattern = ".*\:1521\:.*"
    app_conf = re.findall(pattern, data)
    if app_conf:
        print("\033[31;1m配置文件{file} 有Oracle配置:\033[0m\033[0m".format(file=file))
        print(app_conf)

    # Mysql
    pattern = ".*\:3306.*"
    app_conf = re.findall(pattern, data)
    if app_conf:
        print("\033[31;1m配置文件{file} 有Mysql配置:\033[0m\033[0m".format(file=file))
        print(app_conf)


if __name__ == '__main__':
    config_files = get_config_files(dirpath)  # list
    print(config_files)
    for file in config_files:
        with open(file, "r", encoding="utf-8") as f_r:
            data = f_r.read()
            new_data = data
            new_data = mod_app_config(new_data)
            new_data = mod_redis_config(new_data)
            new_data = mod_rocketmq_config(new_data)
            other_config(new_data)

        if new_data != data:
            # print(file, new_data)
            with open(file, "w", encoding="utf-8") as f_w:
                f_w.write(new_data)
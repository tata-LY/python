#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import xlrd
import json
import re
import os

def print_domain(domain_list):
    dns_conf = "dns_conf.txt"
    web_domain = []
    web_data = '# web domain name\n'
    service_domian = []
    service_data = '# service domain name\n'
    for domain in domain_list:
        if re.match(".*\.web\..*", domain):
            web_domain.append(domain)
            web_data += "172.25.2.53\t" + domain + '\n'
        elif re.match(".*\.service\..*", domain):
            service_domian.append(domain)
            service_data += '172.25.2.54\t' + domain + '\n'
        else:
            print("域名{domain}不合法！".format(domain=domain))

    # print(web_data, service_data)
    with open(dns_conf, "w", encoding="utf-8") as f_w:
        f_w.write(web_data + service_data)

if __name__ == '__main__':
    excel_conf = "conf.xlsx"
    json_conf = "conf.json"
    workbook = xlrd.open_workbook(excel_conf)
    Data_sheet = workbook.sheets()[0]
    rowNum = Data_sheet.nrows  # sheet行数
    colNum = Data_sheet.ncols  # sheet列数

    # print(rowNum, colNum)
    # print(Data_sheet.cell_value(0, 0))

    # 获取所有单元格的内容
    conf_dict = {}
    domain_list = []
    for i in range(rowNum):
        app_name = Data_sheet.cell_value(i, 0)
        domain_name = Data_sheet.cell_value(i, 1)

        domain_list.append(domain_name)

        if Data_sheet.cell_value(i, 2):
            http_port = str(int(Data_sheet.cell_value(i, 2)))
        if Data_sheet.cell_value(i, 3):
            https_port = str(int(Data_sheet.cell_value(i, 3)))
        conf_dict[app_name] = {
            "app_name": app_name,
            "domain_name": domain_name,
            "http_port": http_port,
            "https_port": https_port,
        }
    # print(conf_dict)
    with open(json_conf, "w", encoding="utf-8") as f_w:
        f_w.write(json.dumps(conf_dict))

    print(domain_list)
    print_domain(domain_list)
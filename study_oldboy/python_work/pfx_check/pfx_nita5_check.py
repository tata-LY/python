#!/usr/bin/env python3
# _*_coding:UTF-8_*_
# by liuyang

import os
import hashlib
moban_dir = "moban"

def md5sum(filename):
    d = hashlib.md5()
    with open(filename, 'rb') as file:
        while 1:
            data = file.read()
            if data:
                d.update(data)
            else:
                break
    return d.hexdigest()

def get_mb_md5():
    mb_md5 = {}
    for maindir, subdir, file_name_list in os.walk(moban_dir):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            dq = filename.split('.')[0]
            file_md5 = md5sum(apath)
            # print(dq, dq_md5)
            mb_md5[dq] = file_md5
    return mb_md5

def get_tax_dq(tax_dq, project):
    config = project + '_taxofcity.txt'
    project_tax_dq = {}
    with open(config, 'r', encoding='utf-8') as f_r:
        for line in f_r:
            tax = line.split()[2]
            dq = line.split()[1]
            project_tax_dq[tax] = dq
    tax_dq[project] = project_tax_dq
    return tax_dq

def pfx_check(mb_md5, tax_dq, project):
    pfx_dir = project + '_pfx'
    for maindir, subdir, file_name_list in os.walk(pfx_dir):
        if maindir == pfx_dir:
            for tax in subdir:
                nita5_file_path = os.path.join(maindir, tax, 'nita5.pdf')
                nita5_md5 = md5sum(nita5_file_path)
                if tax in tax_dq[project]:
                    dq = tax_dq[project][tax]
                    #print(nita5_md5, mb_md5[dq])
                    if dq in mb_md5:
                        if nita5_md5 != mb_md5[dq]:
                            print("{project} 地区{dq} 税号{tax} nita5.pd文件md5不匹配。".format(project=project, dq=dq, tax=tax))
                    else:
                        print("{project} 地区{dq} 税号{tax}  在模板文件里不存在。".format(project=project, dq=dq, tax=tax))
                else:
                    print("{project} 税号{tax} 在税号省份表里不存在。".format(project=project, tax=tax, dq=dq))


if __name__=='__main__':
    mb_md5 = {}
    tax_dq = {}
    mb_md5 = get_mb_md5()
    tax_dq = get_tax_dq(tax_dq, 'dx')
    tax_dq = get_tax_dq(tax_dq, 'lt')
    # print(mb_md5)
    #for key, value in tax_dq.items():
    #    print(key, value)

    pfx_check(mb_md5, tax_dq, 'dx')
    pfx_check(mb_md5, tax_dq, 'lt')
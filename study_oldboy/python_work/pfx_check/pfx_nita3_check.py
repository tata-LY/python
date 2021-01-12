#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import hashlib
import os

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

def pfx_check(project, mb_md5):
    pfx_dir = project + '_pfx'
    for maindir, subdir, file_name_list in os.walk(pfx_dir):
        if maindir == pfx_dir:
            for tax in subdir:
                inta3_file = os.path.join(maindir, tax, 'nita3.pdf')
                inta3_file_md5 = md5sum(inta3_file)
                if inta3_file_md5 != mb_md5:
                    print("{project}项目 税号{tax} nita3.pdf md5值不匹配".format(project=project, tax=tax))

if __name__ == '__main__':
    mb_name = '应征货物劳务清单.pdf'
    mb_file = os.path.join('moban', mb_name)
    mb_md5 = md5sum(mb_file)

    pfx_check('dx', mb_md5)

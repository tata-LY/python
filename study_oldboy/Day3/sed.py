#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import sys, os

def file_ok(file_name):
    if not os.path.exists(file):
        exit("ERROR: {file} is not exists!".format(file=file))
    else:
        if not os.path.isfile(file):
            exit("ERROR: {file} is not a file!".format(file=file))

def file_str_replace(before_str, after_str, file):
    f_r = open(file, "r", encoding="utf-8")
    data = ""
    for line in f_r:
        data += line.replace(before_str, after_str )
    f_r.close()
    f_w = open(file, "w", encoding="utf-8")
    f_w.write(data)
    f_w.close()

if len(sys.argv) == 4:
    before_str = sys.argv[1]
    after_str = sys.argv[2]
    file = sys.argv[3]
    file_ok(file)
    file_str_replace(before_str, after_str, file)
    if sys.argv[1] in ["--help", "-h"]:
        exit("Usage: sed.py [OPTION] [OPTION] [FILE]")
else:
    exit("Usage: sed.py [OPTION] [OPTION] [FILE]")


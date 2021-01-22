#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import sys, os, new_dir.input_mode

# print(sys.path)
print("### sys.argv")
print(sys.argv)

print("\n### os.system")
free_result = os.system('free -m')
print(free_result)

print("\n### os.popen")
free_result = os.popen('free -m').read()
print(free_result)
print(type(free_result))

if os.path.isdir('new_dir'):
    os.system('dir new_dir')
else:
    os.mkdir('new_dir')

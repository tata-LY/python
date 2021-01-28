#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 14:16
# @Author  : liuyang
# @File    : 05_module_os.py
# @Software: PyCharm

import os

print(os.getcwd())  # 当前目录

# os.chdir("C:") # 切换目录
# print(os.getcwd())  # C:\
# os.chdir(r"C:")
# print(os.getcwd())  # C:\
#
# print(os.curdir)  # 当前目录    .
# print(os.pardir)  # 上一级目录   ..

# os.makedirs(r"C:\a\b")  # 递归创建目录
# os.removedirs(r"C:\a\b") # 递归删除空目录

# os.mkdir(r"C:\a")  # 创建目录（不递归）
# os.rmdir(r"C:\a") # 直接删除一个目录

# os.remove("test.txt") # 删除一个文件
# os.rename("oldname","newname")  重命名文件/目录

print(os.listdir(r"E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day5")) # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

print(os.stat(os.getcwd() + '\\' +  'readme.md'))  # 获取文件/目录信息  os.stat_result(st_mode=33206, st_ino=3659174697266453, st_dev=1822864103, st_nlink=1, st_uid=0, st_gid=0, st_size=119, st_atime=1611728236, st_mtime=1611728236, st_ctime=1611708285)

print(os.sep) # 系统目录分隔符     '\'
print(os.linesep) # 系统换行分隔符     ’\r\n‘
print(os.pathsep) # 输出用于分割文件路径的字符串      ';'

print(os.environ) # 系统环境变量
for item in os.environ.items():
    print(item)

print(os.name)  # nt 当前使用平台 win=nt

# os.system('ipconfig')  # 执行系统命令

print(os.path.abspath('readme.md'))  # 获取文件的绝对路径 E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day5\readme.md

print(os.path.split(os.path.abspath('readme.md'))) # ('E:\\刘洋工作\\20200921\\git\\tata-LY\\python\\study_oldboy\\Day5', 'readme.md')
print(os.path.dirname(os.path.abspath('readme.md'))) # 获取文件当前目录名称 E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day5
print(os.path.basename(os.path.abspath('readme.md'))) # 只取文件名 readme.md

print(os.path.exists('readme.md'))  # True
print(os.path.exists('module_test')) # 判断目录 False

print(os.path.isabs('readme.md'))  # 是否是绝对路径    False
print(os.path.isabs(os.path.abspath('readme.md')))  # True
print(os.path.isabs("/a/b"))    # True

print(os.path.isfile("C:\\"))  # 判断是否是文件    False
print(os.path.isdir("C:\\"))  # 判断是否是目录     True

print(os.path.join("C:", "/a.txt")) # 目录拼接 C:/a.txt
print(os.path.getatime('readme.md'))  # 返回path所指向的文件或者目录的最后存取时间 1611728236.265293
print(os.path.getmtime('readme.md'))  # 返回path所指向的文件或者目录的最后修改时间 1611728236.265293

dir_name = 'E:\\刘洋工作\\20200921\\git\\tata-LY\\python\\study_oldboy\\Day5'
for root, dirs, files in os.walk(dir_name):
    print(root, dirs, files)
    exit()
"""
os.walk()遍历目录所有的目录和文件，输出格式：‘根目录,根目录下目录列表，根目录下文件列表’参考如下：
E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day5 ['01_module_test', 'day5', 'package_test', 'work'] ['02_package_test.py', '03_module_time.py', '04_module_random.py', '05_module_os.py', 'configparser1.conf', 'configparser2.conf', 'module.shutil.py', 'module_configparser1.py', 'module_configparser2.py', 'module_configparser3.py', 'module_hashlib.py', 'module_json_pickle.py', 'module_os.py', 'module_pyyaml.py', 'module_re.py', 'module_shelve.py', 'module_sys.py', 'module_xml1.py', 'module_xml2.py', 'module_xml3.py', 'output.xml', 'python时间转换.png', 'readme.md', 'shelve_test1.bak', 'shelve_test1.dat', 'shelve_test1.dir', 'shutil_archive.zip', 'shutil_file1.txt', 'xml1.xml', 'xml2.xml', '__init__.py', '概念介绍']
"""

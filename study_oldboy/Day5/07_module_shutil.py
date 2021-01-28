#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 14:56
# @Author  : liuyang
# @File    : 07_module_shutil.py
# @Software: PyCharm

import shutil

f_r = open("readme.md", "r", encoding="utf-8")
f_w = open("07_shutil_file1.txt", "w", encoding="utf-8")
# shutil.copyfileobj(fsrc, fdst[, length])
shutil.copyfileobj(f_r, f_w)    # 将文件内容拷贝到另一个文件中，可以部分内容
f_r.close()
f_w.close()

# shutil.copyfile(src, dst) # 拷贝文件,不拷贝权限
shutil.copyfile('07_shutil_file1.txt', '07_shutil_file1_copyfile.txt')

# shutil.copymode(src, dst)     # 仅拷贝权限。内容、组、用户均不变
shutil.copymode('__init__.py', '07_shutil_file1_copyfile.txt')

# shutil.copystat(src, dst) # 拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat('readme.md', '07_shutil_file1.txt')

# shutil.copy(src, dst) # 拷贝文件和权限
shutil.copy('07_shutil_file1.txt', '07_shutil_file1_copy.txt')

# shutil.copy2(src, dst)    # 拷贝文件和状态信息
shutil.copy2('07_shutil_file1.txt', '07_shutil_file1_copy2.txt')


# shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件
"""cp -r src dst"""
# shutil.ignore_patterns(*patterns) # 忽略哪个文件，有选择性的拷贝,参考下面例子
# shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) # folder1拷贝成folder2，忽略*.pyc、tmp*的文件。

# shutil.rmtree(path[, ignore_errors[, onerror]])
# 递归的去删除文件
"""rm -r src dst"""

# shutil.move(src, dst)
# 递归的去移动文件
"""mv src dst"""


# shutil.make_archive(base_name, format,...)
# 创建压缩包并返回文件路径，例如：zip、tar
#
# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
# 如：www                        =>保存至当前路径
# 如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
# format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir：	要压缩的文件夹路径（默认当前目录）
# owner：	用户，默认当前用户
# group：	组，默认当前组
# logger：	用于记录日志，通常是logging.Logger对象
shutil.make_archive("07_shutil_archive", "zip", "01_module_test")   # 把01_module_test目录压缩成07_shutil_archive.zip
# 打包模块参考zipfile

#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 高级的 文件、文件夹、压缩包 处理模块

import shutil

f_r = open("README", "r", encoding="utf-8")
f_w = open("shutil_file1.txt", "w", encoding="utf-8")

# shutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中，可以部分内容
shutil.copyfileobj(f_r, f_w)

# shutil.copyfile(src, dst)
# 拷贝文件


# shutil.copymode(src, dst)
# 仅拷贝权限。内容、组、用户均不变

# shutil.copystat(src, dst)
# 拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat('README', 'shutil_file1.txt')

# shutil.copy(src, dst)
# 拷贝文件和权限
"""Copy data and mode bits ("cp src dst").

The destination may be a directory.

"""

# shutil.copy2(src, dst)
# 拷贝文件和状态信息
"""Copy data and all stat info ("cp -p src dst").

The destination may be a directory.

"""

# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件
"""cp -r src dst"""

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
shutil.make_archive("shutil_archive", "zip", "module_test")

# import zipfile
# # 压缩
# z = zipfile.ZipFile('laxi.zip', 'w')
# z.write('a.log')
# z.write('data.data')
# z.close()

# # 解压
# z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall()
# z.close()

# import tarfile
#
# # 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
# tar.close()
#
# # 解压
# tar = tarfile.open('your.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()


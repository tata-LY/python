#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 15:20
# @Author  : liuyang
# @File    : 08_module_zipfile.py
# @Software: PyCharm

import tarfile

# 压缩    把01_module_test目录和readme.md文件压缩到08_tarfile.tar
tar = tarfile.open('08_tarfile.tar','w')
tar.add('01_module_test', arcname='01_module_test')
tar.add('readme.md', arcname='readme.md')
tar.close()

# 解压
# tar = tarfile.open('08_tarfile.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()
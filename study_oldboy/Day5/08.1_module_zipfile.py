#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 15:20
# @Author  : liuyang
# @File    : 08_module_zipfile.py
# @Software: PyCharm

import zipfile
# 压缩    把01_module_test目录和readme.md文件压缩到08_zipfile.zip
z = zipfile.ZipFile('08_zipfile.zip', 'w')
z.write('01_module_test')
print('添加了01_module_test到压缩文件08_zipfile.zip')
z.write('readme.md')
print('添加了readme.md到压缩文件08_zipfile.zip')
z.close()

# 解压
# z = zipfile.ZipFile('08_zipfile.zip', 'r')
# z.extractall()    # 可设置解压地址
# z.close()
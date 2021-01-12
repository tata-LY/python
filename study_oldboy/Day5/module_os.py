#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os

print(os.getcwd())  # 当前目录

# os.chdir("F:\\")  # 切换目录
# print(os.getcwd())  # F:\
# os.chdir(r"F:\")
# print(os.getcwd())  # F:\

print(os.curdir)  # 当前目录
print(os.pardir)  # 上一级目录

# os.makedirs(r"F:\a\b")  # 递归创建目录
# os.removedirs(r"F:\a\b") # 删除空目录
#
# os.mkdir(r"F:\a")  # 创建目录（不递归）
# os.rmdir(r"F:\a") # 直接删除一个目录

# os.remove("test.txt") # 删除一个文件
# os.rename("oldname","newname")  重命名文件/目录

print(os.listdir(r"F:\F liuyang 20180409\python\study_oldboy\Day5")) # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.stat(os.getcwd() + '\\' +  'README'))  # 获取文件/目录信息

print(os.sep) # 系统目录分隔符
print(os.linesep) # 系统换行分隔符
print(os.pathsep) # 输出用于分割文件路径的字符串

print(os.environ) # 系统环境变量
for item in os.environ.items():
    print(item)

print(os.name) # nt
os.system('ipconfig /all')  # 执行系统命令

print(os.path.abspath('README'))  # 获取文件的绝对路径 F:\F liuyang 20180409\python\study_oldboy\Day5\README
print(os.path.split(os.path.abspath('README'))) # ('F:\\F liuyang 20180409\\python\\study_oldboy\\Day5', 'README')
print(os.path.dirname(os.path.abspath('README'))) # 获取文件当前目录名称 F:\F liuyang 20180409\python\study_oldboy\Day5
print(os.path.basename(os.path.abspath('README'))) # 只取文件名 README

print(os.path.exists('README'))
print(os.path.exists('module_test')) # 也能判断目录

print(os.path.isabs('README'))  # 是否是绝对路径
print(os.path.isabs(os.path.abspath('README')))
print(os.path.isabs("/a/b"))

print(os.path.isfile("C:\\"))  # 判断是否是文件
print(os.path.isdir("C:\\"))  # 判断是否是目录

print(os.path.join("C:", "/a.txt"))
print(os.path.getatime('README'))  # 返回path所指向的文件或者目录的最后存取时间 1538200999.370619
print(os.path.getmtime('README'))  # 返回path所指向的文件或者目录的最后修改时间 1538200999.3716192
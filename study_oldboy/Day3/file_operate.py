#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

lyrics_file = "lyrics"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

f_r = open(lyrics_file, encoding="utf-8")  # 文件句柄  默认为 "r" 模式,只读
print(f_r)
data = f_r.read()
data2 = f_r.read()   # 读取不到了
f_r.close()
print(data2)

f_w = open(lyrics_file2, "w", encoding="utf-8")   #"w" 模式是覆盖,不能读
f_w.write("Over\n")
f_w.close()

f_a = open(lyrics_file, "a", encoding="utf-8")     # "a" 模式是追加，不能读
#f_a.write("Over")
#data = f_a.read()
f_a.close()

# 显示前五行
f_r = open(lyrics_file, "r", encoding="utf-8")
for i in range(5):
    print(f_r.readline())
f_r.close()

# readlines 读取文件存放在内存里，适合小文件
f_r = open(lyrics_file, "r", encoding="utf-8")
# print(f_r.readlines())
for line in f_r.readlines():
    print(line.rstrip())
f_r.close()

f_r = open(lyrics_file, "r", encoding="utf-8")
print("-".center(30, "-"))
for index,item in enumerate(f_r.readlines()):
    print(index,item.rstrip())
f_r.close()

# 一行行读，内存里只存一行的值,自己加个变量自增来记录行数
count = 0
f_r = open(lyrics_file, "r", encoding="utf-8")
for line in f_r:
    count += 1
    print(count, line.rstrip())
f_r.close()

# 文件读取位置
f_r = open(lyrics_file, "r", encoding="utf-8")
print(f_r.tell())
print(f_r.read(5))
print(f_r.readline())
print(f_r.tell())
print(f_r.seekable()) # 是否可以移动
f_r.seek(0)   # 位置移到文件最开始的地方
print(f_r.readline())
print(f_r.encoding)   # 文件编码
print(f_r.name)  # 文件名字
f_r.close()


f_w = open(lyrics_file2, "w", encoding="utf-8")
f_w.write("Over\n")
f_w.flush()     # 写文件时，强制性flush到硬盘，避免数据丢失(通过python终端可以很好看到结构)
f_w.close()

f_a =  open(lyrics_file2, "a", encoding="utf-8")
f_a.seek(10)
# f_a.truncate(10)   # 截断位置后的10个字节
f_a.close()

f = open(lyrics_file, "r+", encoding="utf-8")   # "r+" 模式是读写
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("Over\n")
f.close()

f = open(lyrics_file2, "w+", encoding="utf-8")   # "w+" 模式是写读
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("New Over\n")
f.write("New Over\n")
f.write("New Over\n")
f.close()

f = open(lyrics_file2, "a+", encoding="utf-8")   # "a+" 模式是追加读  跟 "r+" 差不多
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("New Over\n")
f.close()

f = open(lyrics_file2, "rb")  # 读二进制的文件,比如网络二进制传输
print(f.read())
f.close()

#f = open(lyrics_file2, "wb")
f = open(lyrics_file2, "ab")
f.write("Hello Liuyang\n".encode())  # 二进制格式写入
f.close()

# So much I need to say
f_r = open(lyrics_file, "r", encoding="utf-8")
f_w = open(lyrics_file3, "w", encoding="utf-8")
for line in f_r:
    if line == "So much I need to say\n":
        line = line.replace("I", "liuyang")
        f_w.write(line.upper())
    else:
        f_w.write(line)
f_r.close()
f_w.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-11 10:41
# @Author  : liuyang
# @File    : 6.py
# @Software: PyCharm
"""
练习6：打印杨辉三角。
"""
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# print(os.path.abspath(__file__))    # E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day4\work\Atm\bin\atm.py
# print(os.path.dirname(os.path.abspath(__file__)))   # E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day4\work\Atm\bin
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # E:\刘洋工作\20200921\git\tata-LY\python\study_oldboy\Day4\work\Atm

from core import main
main.run()
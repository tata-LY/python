#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-5 13:58
# @Author  : liuyang
# @File    : ftp_client.py
# @Software: PyCharm
import socket
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class selectFtpClient():

    def __init__(self):
        self.createSocket()
        self.command_out()

    def createSocket(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(("127.0.0.1", 8885))
            print('连接FTP服务器成功!')
        except Exception as e:
            print("error: ", e)

    def command_out(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'exit':
                break
            cmd, file = cmd.split()
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(cmd, file)
            else:
                print('调用错误!')

    def get(self, cmd, file):
        pass

    def put(self, cmd, file):
        if os.path.isfile(file):
            fileName = os.path.basename(file)
            fileSize = os.path.getsize(file)
            fileInfo = '%s|%s|%s' % (cmd, fileName, fileSize)
            self.client.send(bytes(fileInfo, encoding='utf8'))
            recvStatus = self.client.recv(1024)
            print('recvStatus', recvStatus)
            hasSend = 0
            if str(recvStatus, encoding='utf8') == "OK":
                with open(file, 'rb') as f:
                    while fileSize > hasSend:
                        contant = f.read(1024)
                        recv_size = len(contant)
                        self.client.send(contant)
                        hasSend += recv_size
                        s = str(int(hasSend / fileSize * 100)) + "%"
                        print("正在上传文件：" + fileName + "   已经上传：" + s)
                print('%s文件上传完毕' % (fileName,))
        else:
            print('文件不存在')


if __name__ == '__main__':
    c = selectFtpClient()
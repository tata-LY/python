#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-4 14:12
# @Author  : liuyang
# @File    : 3.1_socket_server_基本.py
# @Software: PyCharm
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).decode("utf-8")
                print("%s wrote:" % self.client_address[0])
                print(self.data)
                self.request.send(self.data.upper().encode("utf-8"))
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    # Create the server, binding to localhost on port 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)  # 单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)    # 多线程
    server.serve_forever()

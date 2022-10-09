# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: server.py 
@time: 2018/10/19
@github: github.com/ronething 

Less is more.
"""

import socket
import time
import threading


def tcplink(sock, addr):
    print("Accept new connection from {0} ...".format(addr))
    sock.send(b"Welcome")
    while True:
        data = sock.recv(1024).decode()
        time.sleep(1)
        if data == "exit" or not data:
            break
        sock.send("Hello, {0}".format(data).encode())

    sock.close()
    print("Connection from {0} closed".format(addr))


host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

if __name__ == '__main__':
    while True:
        # 接受一个新连接
        sock, addr = s.accept()
        # 创建线程来处理 TCP 连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

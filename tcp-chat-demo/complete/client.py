# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: client.py 
@time: 2018/10/19
@github: github.com/ronething 

Less is more.
"""

import socket


s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print("Linked")
info = ""
while info != "exit":
    print("From Others: {0}".format(info))
    send_mes = input("输入内容发送: ")
    s.send(send_mes.encode())
    if send_mes == "exit":
        break
    info = s.recv(1024).decode()
s.close()
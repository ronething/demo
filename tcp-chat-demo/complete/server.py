# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: server.py 
@time: 2018/10/19
@github: github.com/ronething 

Less is more.
"""

import socket


host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print("Linked")
info = sock.recv(1024).decode()
while info != "exit":
    print("From Others: {0}".format(info))
    send_mes = input("输入内容发送: ")
    sock.send(send_mes.encode())
    if send_mes == "exit":
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()
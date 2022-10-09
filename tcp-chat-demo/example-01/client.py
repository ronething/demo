# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@file: client.py 
@time: 2018/10/19
@github: github.com/ronething 

Less is more.
"""

import socket


host = socket.gethostname()
port = 12345
print(host)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect((host, port))
# 接受欢迎消息
print(s.recv(1024).decode())
for data in ["Mike", "ronething", "_Shiyeye" , "别说了"]:
    # 发送数据
    s.send(data.encode())
    print(s.recv(1024).decode())
s.send(b"exit")
s.close()

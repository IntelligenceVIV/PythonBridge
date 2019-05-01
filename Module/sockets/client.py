# @Time    : 2019/4/25 10:53
# @Author  : Noah
# @File    : client.py
# @Software: PyCharm
# @description: simple client

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))

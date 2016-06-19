#!/bin/bash

echo "Enter network: "
read NETWORK
echo "Enter 3rd octet: "
read THIRD
echo "Enter 4th octet: "
read FOURTH
echo "Enter output host file name: "
read HFNAME

python3.5 generate_hosts.py $NETWORK $THIRD $FOURTH $HFNAME
pssh -i -O StrictHostKeyChecking=no -h $HFNAME -l root -A whoami

#!/bin/bash

VERSION=1.3

function netcatinput {
	echo "OPTIONS / HTTP/1.1"
	echo -e "HOST: 127.0.0.1\n\n"
}

function color {
	GREEN="\033[0;32m"
	CYAN="\033[0;36m"
	GRAY="\033[0;37m"
	BLUE="\033[0;34m"
	YELLOW="\033[0;33m"
	REDBOLD="\033[1;91m"
	NORMAL="\033[m"
	color=\$${1:-NORMAL}
	echo -ne "`eval echo ${color}`"
	cat
	echo -ne "${NORMAL}"
}

clear

while true
do
	cat << "EOF"
 ____ ___  ___ _ _ _ ____ _                                        
 [__] |--'  |  | _X_ |--| |___                                     
 ___  ____ __ _ __ _ ____ ____   ____ ____ ____ ___  ___  ____ ____
 |==] |--| | \| | \| |=== |--<   |__, |--< |--| |==] |==] |=== |--<

EOF
	
	echo -e "HTTP Web Server Banner Grabber\nMade by Shawn Pang, DISM SP\nVersion $VERSION | 28 May, 2016\n"

	echo -e "[1]\t-\tSimple Banner Grab"
	echo -e "[2]\t-\tSimple Banner Grab (Loop and Output)"
	echo -e "[3]\t-\tFull Banner Grab (Longer)"
	echo -e "[C]\t-\tClear Screen (Removes Past Grabs)"
	echo -e "[Q]\t-\tExit\n"
	echo -e "Press a key to continue\n"
	i=0
	while [ "$i" -eq 0 ]
	do
		read -rsn1 key
		case $key in
			1)
				echo -e "Selected: [1] Simple Banner Grab"
				echo -n "Enter target host: "
				read HOST
				echo -e "Grabbing $HOST's information...\n"
				
				netcatinput | netcat -q 2 $HOST 80 | cat | grep -E 'Server:|Powered-By:' | color REDBOLD
				
				echo -e "\n"
				i=1
				sleep 1
				;;
			2)	
				echo -e "Selected: [2] Simple Banner Grab (Loop and Output)"
				echo -n "Enter output file name: "
				read OUTPUTFILE

				while true
				do			
					echo -n "Enter target host (enter q to quit): "
					read HOST
					if [ "$HOST" = "q" ]
					then
						i=1					
						break
					fi
					echo -e "\nGrabbing $HOST's banner...\n"
				
					echo "$HOST:" >> $OUTPUTFILE
					netcatinput | netcat -q 2 $HOST 80 | cat | grep -E 'Server:|Powered-By:' | tee -a $OUTPUTFILE
					echo "" >> $OUTPUTFILE		
				
					echo ""
				done
				;;			
			3)
				echo -e "Selected: [3] Full Banner Grab (Longer)"
				echo -n "Enter target host: "
				read HOST
				echo -e "\nGrabbing $HOST's banner...\n"
				
				netcatinput | netcat -q 5 $HOST 80 | cat | color CYAN
				
				echo ""
				i=1
				sleep 1
				;;
			c)
				clear
				i=1
				;;
			q)	
				exit;;
		esac
	done
done



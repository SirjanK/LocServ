#!/usr/bin/env bash
echo "Enter the desired port number above 1024 (eg. 5000):"
read port_number
re='^[0-9]+$'
if ! [[ $port_number =~ $re ]] ; then
    echo "error: Not a number" >&2; exit 1
fi
if [ "$port_number" -lt "1025" ]; then
    echo error: Port number is not above 1024; exit 1
fi
python3 LocServ.py -p $port_number &
nohup ngrok http $port_number &
sleep 1
curl localhost:4040/api/tunnels/ | ngrok_url=$(python3 ngrok_url.py)

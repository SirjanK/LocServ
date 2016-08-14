#!/usr/bin/env bash
echo "Enter the port number of the server"
read port_number
re='^[0-9]+$'
if ! [[ ${port_number} =~ $re ]] ; then
    echo "error: Not a number" >&2; exit 1
fi
kill -9 $(lsof -i:4040 -t)
kill -9 $(lsof -i:${port_number} -t)

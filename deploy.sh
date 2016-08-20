#!/usr/bin/env bash
trap destroy SIGINT
function destroy() {
    kill -9 $(lsof -i:4040 -t)
    kill -9 $(lsof -i:${port_number} -t)
    exit 0
}
echo "Enter the desired port number above 1024 (eg. 5000):"
read port_number
re='^[0-9]+$'
if ! [[ ${port_number} =~ $re ]]; then
    echo "error: Not a number" >&2; exit 1
fi
if [ "$port_number" -lt "1025" ]; then
    echo error: Port number is not above 1024; exit 1
fi
if [ "$port_number" -eq "4040" ]; then
    echo error: Port number will be utilized by ngrok, please choose another one; exit 1
fi
python3 LocServ.py -p ${port_number} &
nohup ngrok http ${port_number} &
sleep 2 #TODO: Update with localhost:4040 being polled for status instead
curl localhost:4040/api/tunnels/ | python3 setup_scripts/ngrok_url.py | python3 setup_scripts/configure_webhook.py
function launch_cancel() {
    echo "Press c to cancel..."
    read -n1 -r -p '' key
    if [ ${key} == "c" ]; then
        destroy
    else
        echo "That's not c -_-"
        launch_cancel
    fi
}
launch_cancel

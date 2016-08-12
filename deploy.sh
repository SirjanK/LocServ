echo "Enter the desired port number (eg. 5000):"
read port_number
re='^[0-9]+$'
if ! [[ $port_number =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi
python LocServ.py -p $port_number

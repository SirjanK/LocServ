import sys
import json


def find_url(json_str):
    ngrok_info = json.JSONDecoder().decode(json_str)
    tunnels_lst = ngrok_info.get('tunnels')
    for tunnel in tunnels_lst:
        tunnel_name = tunnel.get('name')
        if tunnel_name == 'command_line (http)':
            return tunnel.get('public_url') + '/'

if __name__ == '__main__':
    ngrok_json_str = ''
    for line in sys.stdin:
        ngrok_json_str += line
    sys.stdout.write(find_url(ngrok_json_str))

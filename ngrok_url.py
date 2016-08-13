from __future__ import print_function
import sys
import json


def find_url(json_str):
    ngrok_info = json.JSONDecoder().decode(json_str)
    tunnels_lst = ngrok_info.get('tunnels')
    return tunnels_lst[0].get('public_url')

if __name__ == '__main__':
    ngrok_json_str = ''
    for line in sys.stdin:
        ngrok_json_str += line
    print(find_url(ngrok_json_str))

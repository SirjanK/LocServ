import os
import json

CREDENTIALS_FILE_PATH = '../../cred/cred.json'


def grab_credentials():
    if not os.path.isfile(CREDENTIALS_FILE_PATH):
        raise CredentialsNotFoundException()
    else:
        credentials_file = open(CREDENTIALS_FILE_PATH)
        credentials_json_str = ''
        for line in credentials_file:
            credentials_json_str += line
        credentials_json = json.JSONDecoder().decode(credentials_json_str)
        return credentials_json


class CredentialsNotFoundException(Exception):
    def __init__(self):
        self.msg = 'App Credentials not found! Make sure to run initial setup.'

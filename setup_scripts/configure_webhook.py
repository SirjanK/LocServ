from __future__ import print_function

import os
import sys

from twilio.rest import TwilioRestClient

sys.path.append(os.getcwd())
from locserv.credentials import grab_credentials

APP_ID_FILE_PATH = './cred/'
APP_ID_FILE_NAME = 'twiml_app_id.txt'


def configure_webhook(client, url):
    complete_file_path = APP_ID_FILE_PATH + APP_ID_FILE_NAME
    if os.path.isfile(complete_file_path):
        app_id_file = open(complete_file_path)
        app_id = app_id_file.read()
        app = client.applications.get(app_id)
        if app:
            client.applications.update(app_id, sms_url=url)
            print(url)
        else:
            os.remove(APP_ID_FILE_PATH)  # App ID is not valid anymore
            generate_new_application(client, url)
    else:
        generate_new_application(client, url)


def generate_new_application(client, url):
    app = client.applications.create(friendly_name='messaging_webhook',
                                     sms_url=url,
                                     sms_method='POST')
    new_file = open(APP_ID_FILE_PATH, 'w')
    new_file.write(app.sid)
    print('Please setup your phone number with this TwiML application now')

if __name__ == '__main__':
    credentials_holder = grab_credentials()
    twilio_client = TwilioRestClient(credentials_holder.get('TWILIO_ACCOUNT_ID'), credentials_holder.get('TWILIO_AUTH_TOKEN'))
    ngrok_url = ''
    for line in sys.stdin:
        ngrok_url += line
    configure_webhook(twilio_client, ngrok_url)

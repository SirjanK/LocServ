from __future__ import print_function

import os
import sys

from twilio.rest import TwilioRestClient

from utils import credentials

APP_ID_FILE_PATH = '../credentials/twiml_app_id.txt'


def configure_webhook(client, url):
    if os.path.isfile(APP_ID_FILE_PATH):
        app_id_file = open(APP_ID_FILE_PATH)
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
    credentials_holder = credentials.grab_credentials()
    twilio_client = TwilioRestClient(credentials_holder.TWILIO_ACCOUNT_ID, credentials_holder.TWILIO_AUTH_TOKEN)
    ngrok_url = ''
    for line in sys.stdin:
        ngrok_url += line
    configure_webhook(twilio_client, ngrok_url)

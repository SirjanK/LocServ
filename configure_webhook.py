from __future__ import print_function
from twilio.rest import TwilioRestClient
import sys
import os

APP_ID_FILE_PATH = './app_id.txt'


def configure_webhook(client, url):
    if os.path.isfile(APP_ID_FILE_PATH):
        app_id_file = open(APP_ID_FILE_PATH)
        app_id = app_id_file.read()
        app = client.applications.get(app_id)
        if app:
            client.applications.update(app_id, sms_url=url, sms_method='GET')
        else:
            os.remove(APP_ID_FILE_PATH)  # App ID is not valid anymore
            generate_new_application(client, url)
    else:
        generate_new_application(client, url)


def generate_new_application(client, url):
    app = client.applications.create(friendly_name='messaging_webhook',
                                     sms_url=url,
                                     sms_method="GET")
    new_file = open(APP_ID_FILE_PATH, 'w')
    new_file.write(app.sid)
    print('Please setup your phone number with this TwiML application now')

if __name__ == '__main__':
    account = "AC01c28726d1857eb4ed815b5cf8a7f51b"
    token = "cfb125802b98e767edb6a98015ca1efa"
    twilio_client = TwilioRestClient(account, token)
    ngrok_url = ''
    for line in sys.stdin:
        ngrok_url += line
    configure_webhook(twilio_client, ngrok_url)

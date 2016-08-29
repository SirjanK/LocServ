from __future__ import print_function

from optparse import OptionParser

import twilio.twiml
from flask import Flask, request
import sys
import os
sys.path.append(os.getcwd())
from locserv import credentials

loc_serve_app = Flask(__name__)


@loc_serve_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    from_number = request.values.get('From', None)
    cred = credentials.grab_credentials()
    print(from_number)
    print(cred.get('PERSONAL_PHONE'))
    if from_number == cred.get('PERSONAL_PHONE'):
        message = 'ayy what is up Sirjan'
    else:
        message = 'wtf who are you'

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="portnum",
                      help="Enter port number for server", metavar=False)
    options, args = parser.parse_args()
    if options.portnum is None:
        loc_serve_app.run(debug=True)
    else:
        PORT = int(options.portnum)
        loc_serve_app.run(host=None, port=PORT, debug=True)

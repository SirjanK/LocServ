from __future__ import print_function
from flask import Flask, request
from optparse import OptionParser
import twilio.twiml

loc_serve_app = Flask(__name__)


@loc_serve_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    from_number = request.values.get('From', None)
    if from_number == '+19729002931':
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
    PORT = int(options.portnum)
    loc_serve_app.run(host=None, port=PORT)

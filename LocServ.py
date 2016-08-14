from __future__ import print_function
from flask import Flask
from optparse import OptionParser
import twilio.twiml

loc_serve_app = Flask(__name__)


@loc_serve_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    message = 'WORKING'
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

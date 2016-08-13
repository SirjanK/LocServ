from __future__ import print_function
from twilio.rest.ip_messaging import TwilioIpMessagingClient

account = "AC01c28726d1857eb4ed815b5cf8a7f51b"
token = "cfb125802b98e767edb6a98015ca1efa"
client = TwilioIpMessagingClient(account, token)

services = client.services.list()
print(services)

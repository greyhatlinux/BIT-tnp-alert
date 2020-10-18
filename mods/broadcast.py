
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

receiver = sys.argv[1]

message = Mail(
    from_email='<registered email with email server>',
    to_emails=receiver,
    subject='Sending T&P updates with Twilio SendGrid',
    html_content='<strong>You have got an update from Training and Placement. Check http://placement.bitmesra.ac.in </strong>')

try:
    sg = SendGridAPIClient('<your api key>')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)



import os
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

 
receiver = sys.argv[1]
msg = sys.argv[2]

msg = msg + " check the portal at http://placemet.bitmesra.ac.in. All the best!"
message = Mail(
    from_email='<registered-email-id>',
    to_emails=receiver,
    subject='Urgent T&P updates',
    html_content=msg )
try:
    sg = SendGridAPIClient('API Key')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

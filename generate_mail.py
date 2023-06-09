# Import smtplib for the actual sending function
import smtplib
import os

# Import the email modules we'll need
from email.message import EmailMessage

textfile = os.getcwd() + "/mail_template.txt"

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())
    msg.add_header("x-appid", "TG-TEST-12345")
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = "ubuntu@calypso-event.net"
msg['To'] = "jeanchristophe.ledez@orange.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
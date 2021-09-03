#!/usr/bin/env python3
from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass


# smtpserver="smtp.gmail.com:587" # TLS port
smtpserver="smtp.gmail.com:465" # SSL port

sender = "sender@example.com"
recipient = "recipient@example.com"
body = "Dear lala,\nthis is a email from me.\nThank you for your attention.\n\nBest regards"

msg = EmailMessage()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = f"Email from {sender} to {recipient}"

msg.set_content(body)

print(msg)

mail_server = smtplib.SMTP_SSL(smtpserver)
# mail_server.set_debuglevel(1)

mail_pass = getpass.getpass('Password? ')

mail_server.login(sender, mail_pass)
mail_server.send_message(msg)
mail_server.quit()

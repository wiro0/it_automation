#!/usr/bin/env python3

import os
import datetime
import reports, emails

descriptions_directory = os.path.expanduser("~/supplier-data/descriptions")
os.chdir(descriptions.directory)
dir_content = os.listdir()

if __name__ == "__main__":
    # retrieve pdf report data
    item_list = []
    for item in dir_content:
        if not os.path.isfile(item) or item.startswith("."):
            continue
        with open(item, "r") as file:
            lines = file.readlines()
            item_list.append(lines[0])
            item_list.append("<br/>")
            item_list.append(lines[1])
            item_list.append("<br/><br/>")
    # pdf report data
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(datetime.datetime.now())
    paragraph = "".join(item_list)
    # generate pdf report
    reports.generate_report(attachment, title, paragraph)

    # email data
    sender = "automation@example.com"
    recipient = "".join([os.getlogin(), "@example.com"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"
    # generate and send email report
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)

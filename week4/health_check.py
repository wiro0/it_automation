#!/usr/bin/env python3

import shutil
import psutil
import os
import emails


# email data
sender = "automation@example.com"
recipient = "".join([os.getlogin(), "@example.com"])
body = "Please check your system and resolve the issue as soon as possible."

def disk_usage():
    """Return True, if the current free disk space is lower than 20 percent total"""
    return shutil.disk_usage("/").free / shutil.disk_usage("/").total < 0.2


def free_memory():
    """Return True, if the current RAM is less than 500MB"""
    return psutil.virtual_memory().free / (2**20) < 500


def cpu_usage():
    """Return True, if CPU usage ration is above 1"""
    return psutil.cpu_percent() > 80


def localhost_present():
    """Check for localhost"""
    with open("/etc/hosts", "r") as file:
        text = file.read()
    return "127.0.0.1" not in text


def main():

    checks = [
        (cpu_usage(), "Error - CPU usage is over 80%"),
        (disk_usage(), "Error - Available disk space is less than 20%"),
        (free_memory(), "Error - Available memory is less than 500MB"),
        (localhost_present(), "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    for check, subject in checks:
        if check:
            error_message = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(error_message)


main()

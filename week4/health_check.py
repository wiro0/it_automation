#!/usr/bin/env python3

import shutil
import psutil
import os
import time
import subprocess


# email data
sender = "automation@example.com"
recipient = "".join([os.getlogin(), "@example.com"])
body = "Please check your system and resolve the issue as soon as possible."

def disk_usage():
    """Return True, if the current free disk space is lower than 20 percent total"""
    return shutil.disk_usage("/").free / shutil.disk_usage("/").total < 0.2


def free_memory():
    """Return True, if the current RAM is less than 20%"""
    return psutil.virtual_memory().free / (2**20) > 500


def cpu_usage():
    """Return True, if CPU usage ration is above 1"""
    return psutil.cpu_percent() > 80


def localhost_present():
    """Check for localhost"""
    res = subprocess.run(["grep", "127.0.0.1", "/etc/hosts"])
    return res.returncode != 0


def main():

    checks = [
        (cpu_usage(), "Error - CPU usage is over 80%"),
        (disk_usage(), "Error - CPU usage is over 80%"),
        (free_memory(), "Error - Available memory is less than 500MB"),
        (localhost_present(), "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    everything_ok = True

    for check, subject in checks:
        if check:
            everything_ok = False
            error_message = emails.email_generate(sender, recipient, subject, body)
            emails.send_email(error_message)


while True:
    main()
    time.sleep(60)

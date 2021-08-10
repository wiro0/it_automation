#!/usr/bin/env python3

import os
import requests

keys = ["title", "name", "date", "feedback"]

os.chdir("/data/feedback")
result = os.listdir()

for item in result:
    if os.isfile(item):
        with open (item, "r") as file:
            text = file.readlines()
            for num, line in enumerate(text):
                data[keys[num]] = line

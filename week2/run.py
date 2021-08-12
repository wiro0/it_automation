#!/usr/bin/env python3
"""
A script to retrieve feedback data from a list of text files, format the data
into a dictionary and send it to a web service
"""

import os
import requests

keys = ["title", "name", "date", "feedback"]

os.chdir("/data/feedback")
result = os.listdir()

for item in result:
    if os.path.isfile(item):
        # Read the feedback data from the text files and turn into a dictionary
        print("Processing file:", item)
        with open (item, "r") as file:
            text = file.readlines()
            data = {}
            for num, line in enumerate(text):
                line = line.strip()
                # If-condition to append all lines 3+ to key "feedback"
                if num > 3:
                    data["feedback"] = data.get(feedback) + " " + line
                    continue
                data[keys[num]] = line
        file.close()

    # Send dictionary to django web service via requests.post
    print("Sending data ...")
    for retry in range(5):
        response = requests.post("http://35.239.10.159/feedback/", data=data)
        if response.status_code != 201:
            if retry > 3:
                print("Could not send data from file:", item)
                break
            continue
        else:
            print("Successfull")
            break

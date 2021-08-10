#!/usr/bin/env python3

import os
import requests

keys = ["title", "name", "date", "feedback"]

os.chdir("/data/feedback")
result = os.listdir()

for item in result:
    if os.path.isfile(item):
        print("Processing file:", item)
        with open (item, "r") as file:
            text = file.readlines()
            data = {}
            for num, line in enumerate(text):
                data[keys[num]] = line
        file.close()
    print("Sending data")
    for retry in range(5):
        response = requests.post("http://<IP>/feedback", json=data)
        if response.status_code != "201":
            if retry > 3:
                print("Could not send data from file:", item)
                break
            continue
        else:
            print("... successfull")
            break
    

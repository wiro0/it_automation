#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload"

os.chdir("~/supplier-data/images")
dir_content = os.listdir()

for item in dir_content:
    with open(os.path.join("~/supplier-data/images", item), "rb") as opened:
        request = requests.post(url, files={'file': opened})

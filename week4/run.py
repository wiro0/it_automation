#!/usr/bin/env python3

import requests
import os
import socket


descriptions_path = os.path.expanduser("~/supplier-data/descriptions")
ip = socket.gethostbyname(socket.gethostname())
url = "".join(["http://", ip, "/fruits/"])


def generate_dictionary(item):
    fruit_dic = {}
    with open(item, "r") as file:
        lines = file.readlines()
        fruit_dic["name"] = lines[0]
        fruit_dic["weight"] = int(lines[1][:-3])
        fruit_dic["description"] = " ".join(lines[2:])
        fruit_dic["image_name"] = os.path.splitext(item)[0] + ".jpeg"
    return fruit_dic


# Get all files in target directory
os.chdir(descriptions_path)
dir_content = os.listdir()

# For each file, generate a dictionary from the contents and send it to the
# server
for item in dir_content:
    if not os.path.isfile(item) or item.startswith("."):
        continue
    requests = requests.post(url, data=generate_dictionary(item))

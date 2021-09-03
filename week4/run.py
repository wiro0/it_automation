#!/usr/bin/env python3

import requests
import os

descriptions_path = "~/supplier-data/descriptions"


def generate_dictionary(item):

    if not os.path.isfile(item) or item.startswith("."):
        continue

    fruit_dic = {}
    
    with open(item, "r") as file:
        lines = file.readlines()
        fruit_dic["name"] = lines[0]
        fruit_dic["weight"] = lines[1]
        fruit_dic["description"] = " ".join(lines[2:])
        fruit_dic["image_name"] = os.path.splitext(item)[0] + ".jpg"
    return fruit_dic


# Get all files in target directory
os.chdir(descriptions_path)
dir_content = os.listdir()

# For each file, generate a dictionary from the contents
for item in dir_content:
    generate_dictionary(item)

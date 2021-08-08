#!/usr/bin/env python3

import os
import re
from PIL import Image

# Store the beginning working directory
org_dir = os.getcwd()

# Make directory "images" if it does not exist
if not os.path.isdir("/opt/images"):
    os.chdir("/opt")
    os.mkdir("images")

image_dir = os.path.join(org_dir, "images")
os.chdir(image_dir)
res = os.listdir()

# Iterate through all files in the current working directory and manipulate all
# matching images
for item in res:
    if item.endswith(".jpg"):
        print(item)
        im = Image.open(item)
        im.rotate(90).resize((640,480)).save(os.path.join("/opt/images", item))

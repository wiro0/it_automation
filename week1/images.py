#!/usr/bin/env python3
#
import os
import re
from PIL import Image

# The image directory
image_dir = "/home/pi/git/it_automation/images"

# Create directory for the modified images if it does not exist
if not os.path.isdir("/opt/images"):
    os.chdir("/opt")
    os.mkdir("images")

# Create a list of all files in the image directory
os.chdir(image_dir)
files = os.listdir()

# Iterate through all files in the current working directory and manipulate all
# matching images
for item in files:
    if os.isfile(item) and item.endswith(".jpg"):
        print(item)
        im = Image.open(item)
        im.rotate(90).resize((640,480)).save(os.path.join("/opt/images", item))

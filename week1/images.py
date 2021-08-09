#!/usr/bin/env python3
"""
A program to manipulate images in a directory through the PIL/pillow module and
store the fixed images.
"""

import os
from PIL import Image

# The source image directory
image_dir = "/home/user/images"

new_extension = ".jpg"

# Create directory for the modified images if it does not exist
if not os.path.isdir("/opt/icons"):
    os.chdir("/opt")
    os.mkdir("icons")

# Create a list of all files in the image directory
os.chdir(image_dir)
dir_content = os.listdir()

# Iterate through all content in the image directory and manipulate all files with
# the matching extension.
for item in dir_content:
    if os.path.isfile(item) and not item.startswith("."):
        print("Processing image:", item)
        im = Image.open(item)
        im = im.rotate(90).resize((128,128)).convert("RGB")

        new_name = os.path.splitext(item)[0] + new_extension
        im.save(os.path.join("/opt/icons", new_name))

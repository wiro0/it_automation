#!/usr/bin/env python3
"""
A program to manipulate images in a directory through the PIL/pillow module and
store the fixed images.
"""

import os
import re
from PIL import Image

# The source image directory
image_dir = "/home/test/images"

# The extension of the target images
extension = ".jpg"

# Create directory for the modified images if it does not exist
if not os.path.isdir("/opt/images"):
    os.chdir("/opt")
    os.mkdir("images")

# Create a list of all files in the image directory
os.chdir(image_dir)
dir_content = os.listdir()

# Iterate through all files in the image directory and manipulate all files with
# the matching extension.
for item in dir_content:
    if os.isfile(item) and item.endswith(extension):
        print("Processing image:", item)
        im = Image.open(item)
        im.rotate(90).resize((640,480)).save(os.path.join("/opt/images", item))

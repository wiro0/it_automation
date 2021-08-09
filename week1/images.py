#!/usr/bin/env python3
"""
A program to manipulate images in a directory through the PIL/pillow module and
store the fixed images.
"""

import os
from PIL import Image

# The source image directory
image_dir = "/home/user/images"

# The extension of the target images
old_extension = ".tiff"
new_extension = ".jpeg"

# Create directory for the modified images if it does not exist
if not os.path.isdir("/opt/images"):
    os.chdir("/opt")
    os.mkdir("images")

# Create a list of all files in the image directory
os.chdir(image_dir)
dir_content = os.listdir()

# Iterate through all content in the image directory and manipulate all files with
# the matching extension.
for item in dir_content:
    if os.path.isfile(item) and item.endswith(old_extension):
        print("Processing image:", item)
        im = Image.open(item)
        
        # Create new filename by splitting, splicing old extension and appending the new one
        new_name = "".join(item.split(".")[:-1]) + new_extension
        im.rotate(90).resize((128,128)).save(os.path.join("/opt/images", new_name))

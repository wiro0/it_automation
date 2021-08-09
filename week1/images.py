#!/usr/bin/env python3
"""
A program to manipulate images in a directory through the PIL/pillow module and
store the fixed images.
"""

import os
from PIL import Image


def create_path(new_dir):
    """
    Create path/directory for the modified images if it does not exist
    """
    dirs_list = new_dir.split("/")
    branch = "/"
    for folder in dirs_list:
        new_branch = os.path.join(branch, folder)
        if not os.path.isdir(new_branch):
            os.chdir(branch)
            os.mkdir(folder)
        branch = new_branch

    
# The source image directory
image_dir = "/home/user/images"
new_dir = "/opt/icons"

new_extension = ".jpg"

create_path(new_dir)

# Create a list of all files in the image directory
os.chdir(image_dir)
dir_content = os.listdir()

# Iterate through the files in the directory, process and store as new files
for item in dir_content:
    if os.path.isfile(item) and not item.startswith("."):
        print("Processing image:", item)
        im = Image.open(item)
        im = im.rotate(90).resize((128,128)).convert("RGB")

        new_name = os.path.splitext(item)[0] + new_extension
        im.save(os.path.join("/opt/icons", new_name))

#!/usr/bin/env python3

from PIL import Image
import os

image_path = "~/supplier-data/images"
new_extension = ".jpg"

os.chdir(image_path)
dir_content = os.listdir()

for item in dir_content:
    if not os.path.isfile(item) or item.startswith("."):
        continue
    print("Processing image:", item)
    im = Image.open(item)
    im = im.resize((600,400)).convert("RGB")

    new_name = os.path.splitext(item)[0] + new_extension
    im.save(os.path.join(image_path, new_name))

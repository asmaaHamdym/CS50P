import sys
import PIL
from PIL import Image
import os

try:
    if len(sys.argv)<= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        #tuple of available sufixes
        sufixes=('.jpg','.jpeg','.png')
        #get extentions of first and second file
        first_ext=os.path.splitext(sys.argv[1])[1].lower()
        second_ext=os.path.splitext(sys.argv[2])[1].lower()

        if first_ext not in sufixes or second_ext not in sufixes:
            sys.exit("Invalid input")

        elif first_ext!=second_ext:
            sys.exit('Input and output have different extensions')

        elif (first_ext==second_ext ):

            shirt = Image.open("shirt.png")
            before=Image.open(sys.argv[1])
            size = shirt.size
            resized_image=PIL.ImageOps.fit(before, size)
            resized_image.paste(shirt,shirt)
            resized_image.save(sys.argv[2])


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
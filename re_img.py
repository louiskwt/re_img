import os
import sys
from random import randint
from PIL import Image, ImageOps

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments. Expecting 2 (including file name)")

if len(sys.argv) > 2:
    sys.exit("Too many command line arguments. Expecting 2 (including file name)")

ACCEPTABLE_FILE_TYPE = [".jpg", ".jpeg", ".png"]

def main():
    # check file type
    ext = os.path.splitext(sys.argv[1])[1]
 
    if ext not in ACCEPTABLE_FILE_TYPE:
        sys.exit("Invalid file type. Only 'jpg', 'jpeg', and 'png' are acceptable")
    
    generate_img(ext)


def generate_img(ext):
    try:
        test_file = open(sys.argv[1])
        test_file.close()
    except FileNotFoundError:
        sys.exit("File not found. Please check your file")
    else:
        shirt = Image.open('./asset/shirt.png')
        original = Image.open(sys.argv[1])

        size = shirt.size

        output = ImageOps.fit(original, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        output.paste(shirt, box=None, mask=shirt)

        output.save(f'out_{randint(0, 100)}{ext}')



if __name__ == "__main__":
    main()
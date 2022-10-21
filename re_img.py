import os
import sys
from random import randint
from PIL import Image, ImageOps

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments. Expecting 2 (including file name)")

if len(sys.argv) > 2:
    sys.exit("Too many command line arguments. Expecting 2 (including file name)")

def main():
    # check file type
    ext = os.path.splitext(sys.argv[1])[1]

    check_extension(ext)
    
    generate_img(sys.argv[1], ext)



def check_extension(ext):
    ACCEPTABLE_FILE_TYPE = [".jpg", ".jpeg", ".png"]
    if ext not in ACCEPTABLE_FILE_TYPE:
        sys.exit("Invalid file type. Only 'jpg', 'jpeg', and 'png' are acceptable")

def generate_img(file, ext):
    try:
        test_file = open(file)
        test_file.close()
    except FileNotFoundError:
        sys.exit("File not found. Please check your file")
    else:
        shirt = Image.open('./asset/shirt.png')
        original = Image.open(file)

        size = shirt.size

        output = ImageOps.fit(original, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        output.paste(shirt, box=None, mask=shirt)

        output.save(f'out_{randint(0, 100)}{ext}')

        return True



if __name__ == "__main__":
    main()
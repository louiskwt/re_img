import os
import sys

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

    return print("Hello Re:Img")


def generate_img():
    pass

if __name__ == "__main__":
    main()
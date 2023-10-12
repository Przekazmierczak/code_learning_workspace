from PIL import Image
import sys
import os

first_file_ext = os.path.splitext(sys.argv[1])
second_file_ext = os.path.splitext(sys.argv[2])
allowed_ext = [".jpg", ".jpeg", ".png"]
if len(sys.argv) != 3:
    sys.exit("Command-line have to have 2 arguments")
elif first_file_ext[1] not in allowed_ext or second_file_ext[1] not in allowed_ext:
    sys.exit("Invalid input")
elif first_file_ext[1] != second_file_ext[1]:
    sys.exit("Input and output have different extensions")
else:
    try:
        picture = Image.open(sys.argv[1], mode='r', formats=None)
        shirt = Image.open(sys.argv[2], mode='r', formats=None)
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        picture_new = picture.crop((0, 0, 1200, 1400))
        shirt = shirt.resize((1200, 1400))
        picture_new.paste(shirt, box=shirt, mask=None)
        picture_new.save("picture.png", format="PNG")
        picture.close()
        shirt.close()
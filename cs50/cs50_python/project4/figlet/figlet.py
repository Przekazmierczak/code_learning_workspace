import pyfiglet
import random
import sys

list = pyfiglet.FigletFont.getFonts()

# Print random font
if len(sys.argv) == 1:
    text = input("Input: ")
    random_font = random.choice(list)
    f = pyfiglet.Figlet(font=random_font)
    print(f.renderText(text))
# Print font choosen by user
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in list:
            text = input("Input: ")
            f = pyfiglet.Figlet(font=sys.argv[2])
            print(f.renderText(text))
        else:
            sys.exit(f"{sys.argv[2]} is not supported font")
    else:
        sys.exit("Supported format: text -f/--font font_name")
else:
    sys.exit("Invalid usage")

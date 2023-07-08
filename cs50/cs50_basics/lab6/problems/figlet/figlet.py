from pyfiglet import Figlet
import random
from sys import argv
import sys

figlet = Figlet()
list = figlet.getFonts()
if len(argv) == 3:
    if argv[1] == '-f' or argv[1] == '--font':
        if argv[2] in list:
            text = input('Text: ')
            figlet.setFont(font=argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
elif len(argv) == 1:
    text = input('Text: ')
    randomList = random.choice(list)
    figlet.setFont(font=randomList)
    print(figlet.renderText(text))
else:
    sys.exit('Invalid usage')
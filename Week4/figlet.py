import random
import sys
from pyfiglet import Figlet
figlet = Figlet()


if len(sys.argv) == 1:
    s=input()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    font=figlet.getFonts()
    if sys.argv[1]=='-f'and sys.argv[2] in font:
        s=input()
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    else:sys.exit("Invalid usage")

else: sys.exit("Invalid usage")
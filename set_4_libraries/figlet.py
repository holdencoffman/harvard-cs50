import pyfiglet as pg
import random as rd
import sys

figlet = pg.Figlet() # not sure if making this global is the best approach but it's convenient for now

def gather_font():
    if len(sys.argv) == 1:
        font_int = rd.randint(0, 570) # 571 total font types, Python lists are zero-indexed so retrieve a random index value between 0 and 570, inclusive
    else:
        if (sys.argv[1] not in ('-f', '--font') or sys.argv[2] not in figlet.getFonts()):
            sys.exit('Invalid arguments, first arg must be -f or --font and second arg must be a valid font name')
        else:
            font_int = figlet.getFonts().index(sys.argv[2]) # convert font name to its corresponding index in the font list
    return font_int


def convert_text(response):
    font_int = gather_font()
    font_name = figlet.getFonts()[font_int]
    figlet.setFont(font=font_name)
    return figlet.renderText(response)

def main():
    if len(sys.argv) > 1 and (sys.argv[1] not in ('-f', '--font') or sys.argv[2] not in figlet.getFonts()):
        sys.exit('Invalid arguments, first arg must be -f or --font and second arg must be a valid font name')
    response = input('Please enter text to be converted to the chosen font:\n')
    converted = convert_text(response)
    print(converted)

if __name__ == '__main__':
    main()
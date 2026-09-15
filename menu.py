from ui import reset, green, bold, yellow, red, magenta

def menu_show():
    print(f"""Main menu
  {green + bold}1){reset} Fight
  {green + bold}2){reset} Check inventory
  {green + bold}3){reset} Quit""")
    choice = input("> ")
    return choice

def choose_difficulty():
    print(f"""{green + bold}1){reset} Back
{green}low{reset} / {yellow}mid{reset} / {red}high{reset} / {magenta}elite{reset}""")
    return input("> ")

def backpack_show():
    print(f"""  {green + bold}1){reset} Craft
  {green + bold}2){reset} Back""")
    return input("> ")

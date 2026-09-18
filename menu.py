from ui import reset, green, bold, yellow, red, magenta

def menu_show():
  print(f"""Main menu
  {green + bold}1){reset} Fight
  {green + bold}2){reset} Check inventory
  {green + bold}3){reset} Quit""")
  choice = input("> ")
  return choice

def equip_choice():
  print(f"Enter the exact name of the item you wish to {yellow}equip{reset}")
  choice = input("> ")
  return choice

def gather_area_selection():
  print(f"""Choose area to gather materials from:
  {green + bold}1){reset} River
  {green + bold}2){reset} Forest""")
  choice = input("> ")
  return choice

def choose_difficulty():
    print(f"""{green + bold}1){reset} Back
{green}low{reset} / {yellow}mid{reset} / {red}high{reset} / {magenta}elite{reset}""")
    return input("> ")

def backpack_show():
    print(f"""  {green + bold}1){reset} Craft
  {green + bold}2){reset} Equip
  {green + bold}3){reset} Back""")
    return input("> ")

def stat_menu():
    print(f"""Choose a stat to upgrade
  {green + bold}1){reset} Health
  {green + bold}2){reset} Attack
  {green + bold}3){reset} Armour""")
    choice = input("> ")
    return choice
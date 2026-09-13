import character
import inventory
from ui import reset, bold, green, blue, magenta
import ui

import menu

ui.clear_terminal()
ui.output(f"{blue}{bold}Terminal RPG{reset}")
player = character.Character(input(f"Enter your {magenta}{bold}name{reset}: "))
backpack = inventory.Inventory()
ui.refresh(player)
menu.menu_selection(player, backpack, input(f"""Main menu
  {green}{bold}1){reset} Fight
  {green}{bold}2){reset} Check inventory
  {green}{bold}3){reset} Quit
> """))
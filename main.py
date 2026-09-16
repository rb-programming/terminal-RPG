import character
import inventory
import fight
import ui
import menu
import time

from character import stat_upgrades
from ui import reset, bold, green, blue, magenta

ui.clear_terminal()
ui.output(f"{blue + bold}Terminal RPG{reset}")
player = character.Character(input(f"Enter your {magenta + bold}name{reset}: "))
backpack = inventory.Inventory()
ui.refresh(player)

while True:
  if player.level_up():
    while True:
      choice = menu.stat_menu()
      if choice in stat_upgrades:
        setattr(player, stat_upgrades[choice][0], (getattr(player, stat_upgrades[choice][0]) + stat_upgrades[choice][1]))
        break
      else:
        print('Enter a valid input')
  ui.refresh(player)
  choice = menu.menu_show()
  if choice == '1':
    ui.refresh(player)
    choice = menu.choose_difficulty()
    if choice == '1':
      pass
    else:
      fight.fight(player, backpack, choice)
  elif choice == '2':
    while True:
      ui.refresh(player)
      backpack.show_inventory()
      choice = menu.backpack_show()
      if choice == '1':
        backpack.craftable()
        item = input("What item would you like to craft: ")
        amount = int(input("How many: "))
        backpack.craft_item(item, amount)
        time.sleep(2)
      if choice == '2':
        break
  elif choice == '3':
    break
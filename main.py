import character
import inventory
import item_stats
import gather
import fight
import ui
import menu
import time

from character import stat_upgrades
from ui import reset, bold, green, blue, magenta, yellow, red

ui.clear_terminal()
player = character.Character(input(f"Enter your {magenta + bold}name{reset}: "))
print(f"Greetings, {magenta}{bold}{player.name}{reset}!")
print()
time.sleep(3)
print(f"Before every fight, you will be able to {green}gather{reset} materials.")
time.sleep(3)
print(f"You can choose one of the two areas, {yellow}forest{reset} or {yellow}river{reset}.")
time.sleep(3)
print(f"They both have {magenta}unique{reset} items you {red}cannot{reset} acquire with your might.")
time.sleep(3)
print(f"You will need to gather items for {yellow}stronger{reset} healing items.")
print()
time.sleep(3)
print(f"When level up is available, your character will automatically do it.")
print(f"When this happens, you will have to choose one of the skills listed to turn your character {magenta}stronger{reset}.")
time.sleep(7)
print()
print(f"Now for the {green}crafting{reset} system:")
print(f"Whenever you have enough materials for a certain recipe, it will appear in your backpack")
print(f"so you will have to {yellow}check{reset} it every now and then to see what the recipes are.")
time.sleep(9)
print()
print(f"Now that's it from me. Good {green + bold}luck{reset}!")
time.sleep(5)

ui.clear_terminal()
ui.output(f"{blue + bold}Terminal RPG{reset}")
backpack = inventory.Inventory()
ui.refresh(player)
has_picked = False
while True:
  if player.current_health == 0:
    break
  if player.level_up():
    while True:
      choice = menu.stat_menu()
      if choice == '2':
        setattr(player, stat_upgrades[choice][0], (getattr(player, stat_upgrades[choice][0]) + stat_upgrades[choice][1]))
        setattr(player, 'max_attack', (getattr(player, 'max_attack') + stat_upgrades[choice][1]))
        break
      elif choice in stat_upgrades:
        setattr(player, stat_upgrades[choice][0], (getattr(player, stat_upgrades[choice][0]) + stat_upgrades[choice][1]))
        break
      else:
        print('Enter a valid input')
  if has_picked == False:
    while True:
      choice = menu.gather_area_selection()
      if choice in gather.gather_area:
        gather.gather(choice, backpack)
        has_picked = True
        time.sleep(2)
        break
      else:
        print("Enter valid choice.")
  ui.refresh(player)
  choice = menu.menu_show()
  if choice == '1':
    ui.refresh(player)
    choice = menu.choose_difficulty()
    if choice == '1':
      pass
    else:
      fight.fight(player, backpack, choice)
      has_picked = False
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
        item_stats.equipment_available(backpack)
        player.equip_item(item=menu.equip_choice(), backpack=backpack)
        time.sleep(2)
        pass
      if choice == '3':
        break
  elif choice == '3':
    break
  else:
    print('Enter valid choice')
    time.sleep(2)
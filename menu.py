import ui

from fight import fight
from ui import reset, green, yellow, magenta, red, bold

def menu_selection(player, backpack, choice):
    if choice == '1':
        ui.refresh(player)
        fight(player, backpack, input(f"{green}low{reset} / {yellow}mid{reset} / {red}high{reset} / {magenta}elite{reset}\n> "))
    elif choice == '2':
        backpack.show_inventory(player)
    elif choice == '3':
        pass
    else:
        print("Enter a valid number.")

def backpack_menu(backpack, player, choice):
    if choice == '1':
        ui.refresh(player)
        print("Backpack:")
        for item, amount in backpack.itemdict.items():
            if int(amount) > 0:
                print(item, amount)
        backpack.craft_item(player, input("Which item do you want to craft? "), input("How many? "))
    if choice == '2':
        ui.refresh(player)
        menu_selection(player, backpack, input(f"""Main menu
  {green}{bold}1){reset} Fight
  {green}{bold}2){reset} Check inventory
  {green}{bold}3){reset} Quit
> """))
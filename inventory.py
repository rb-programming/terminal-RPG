import recipes
import ui
import menu

from ui import green, bold, reset

class Inventory:
    def __init__(self, itemdict = {}):
        self.itemdict = itemdict

    def show_inventory(self, player):
        ui.clear_terminal()
        ui.topbar(player)
        print("Backpack:")
        for item, amount in self.itemdict.items():
            if int(amount) > 0:
                print(item, amount)
        menu.backpack_menu(self, player, input(f"""  {green}{bold}1){reset} Craft
  {green}{bold}2){reset} Back
> """))

    def pick_item(self, item, amount):
        if item in self.itemdict:
            self.itemdict[item] += amount
        else:
            self.itemdict[item] = amount

    def delete_item(self, item, amount):
        if item in self.itemdict:
            if self.itemdict[item] < int(amount):
                print(f"You don't have that many {item}.")
            else:
                self.itemdict[item] -= int(amount)
        else:
            print(f"You don't have {item} in your inventory.")

    def craft_item(self, player, item, craft_amount):
        ui.clear_terminal()
        ui.topbar(player)
        x = recipes.Recipe()
        canCraft = True
        if item in x.recipes:
            for component, amount in x.recipes[item].items():
                if component in self.itemdict:
                    if amount * int(craft_amount) > self.itemdict[component]:
                        canCraft = False
                else:
                    canCraft = False
        if canCraft:
            for component, amount in x.recipes[item].items():
                self.delete_item(component, amount * craft_amount)
            self.pick_item(item, 1 * craft_amount)
        else:
            print("You don't have enough materials to craft that item")
        print("Backpack:")
        for item, amount in self.itemdict.items():
            if int(amount) > 0:
                print(item, amount)
        menu.backpack_menu(self, player, input(f"""  {green}{bold}1){reset} Craft
  {green}{bold}2){reset} Back
> """))
import recipes
import ui
import menu

from ui import green, bold, reset

class Inventory:
    def __init__(self, itemdict=None):
        if itemdict == None:
            itemdict = {}
        self.itemdict = itemdict

    def show_inventory(self, player):
        ui.refresh(player)
        print("Backpack:")
        for item, amount in self.itemdict.items():
            if amount > 0:
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
        ui.refresh(player)
        recipe_book = recipes.recipes
        can_craft = True
        if item not in recipe_book:
            print("Enter a valid item")
        elif item in recipe_book:
            for component, amount in recipe_book[item].items():
                if component in self.itemdict:
                    if amount * int(craft_amount) > self.itemdict[component]:
                        can_craft = False
                else:
                    can_craft = False
            if can_craft:
                for component, amount in recipe_book[item].items():
                    self.delete_item(component, amount * craft_amount)
                self.pick_item(item, 1 * craft_amount)
            else:
                print("You don't have enough materials to craft that item")
            print("Backpack:")
        for item, amount in self.itemdict.items():
            if amount > 0:
                print(item, amount)
        menu.backpack_menu(self, player, input(f"""  {green}{bold}1){reset} Craft
  {green}{bold}2){reset} Back
> """))
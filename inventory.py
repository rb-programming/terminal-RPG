import recipes

class Inventory:
    def __init__(self, itemdict=None):
        if itemdict == None:
            itemdict = {}
        self.itemdict = itemdict

    def show_inventory(self):
        print("Backpack:")
        for item, amount in self.itemdict.items():
            if amount > 0:
                print(item, amount)

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

    def craftable(self):
        recipe_book = recipes.recipes
        for item in recipe_book:
            can_craft = True
            components = []
            for component, amount in recipe_book[item].items():
                components.append(f"{amount}x {component}")
                if component not in self.itemdict:
                    can_craft = False
                elif self.itemdict[component] < amount:
                    can_craft = False
            if can_craft:
                print(f"{item} | {', '.join(components)}")

    def craft_item(self, item, craft_amount):
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
                print(f"You have crafted {craft_amount}x {item}")
            else:
                print("You don't have enough materials to craft that item")
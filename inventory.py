import recipes

class Inventory:
    def __init__(self, itemdict = {}):
        self.itemdict = itemdict

    def show_inventory(self):
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
            if self.itemdict[item] < amount:
                print(f"You don't have that many {item}.")
            else:
                self.itemdict[item] -= amount
        else:
            print(f"You don't have {item} in your inventory.")

    def craft_item(self, item, craftAmount):
        x = recipes.Recipe()
        canCraft = True
        if item in x.recipes:
            for component, amount in x.recipes[item].items():
                if component in self.itemdict:
                    if amount * craftAmount > self.itemdict[component]:
                        canCraft = False
                else:
                    canCraft = False
        if canCraft:
            for component, amount in x.recipes[item].items():
                self.delete_item(component, amount * craftAmount)
            self.pick_item(item, 1 * craftAmount)
        else:
            print("You don't have enough materials to craft that item")

        

if __name__ == "__main__":
    backpack = Inventory()
    backpack.pick_item("Bone", 5)
    backpack.pick_item("Sharp Stone", 5)
    backpack.pick_item("Feather", 5)
    backpack.craft_item("Arrow", 5)
    backpack.show_inventory()
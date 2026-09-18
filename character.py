import random
from item_stats import equippable

class Character:
    def __init__(self, name, current_health = 100, max_health = 100, attack = 9, max_attack = 14, crit = 0, attack_speed = 1, armour = 5, xp = 0, level = 1, equipped_weapon = None, equipped_armour = None, equipped_headwear = None, equipped_ring = None):
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.attack = attack
        self.max_attack = max_attack
        self.crit = crit
        self.attack_speed = attack_speed
        self.armour = armour
        self.xp = xp
        self.level = level
        self.equipped_weapon = equipped_weapon
        self.equipped_armour = equipped_armour
        self.equipped_headwear = equipped_headwear
        self.equipped_ring = equipped_ring

    def level_up(self):
        if self.xp >= int(75 * self.level ** 1.6):
            self.xp -= int(75 * self.level ** 1.6)
            self.level += 1
            return True
        return False

    def gain_xp(self, difficulty):
        if difficulty in xp_drop:
            self.xp += random.randint(xp_drop[difficulty][0], xp_drop[difficulty][1])

    def get_damaged(self, amount):
        if self.current_health - amount <= 0:
            self.current_health = 0
        else:
            self.current_health -= amount

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def equip_item(self, item, backpack):
        for category in equippable:
            if item in equippable[category]:
                equipped = getattr(self, slots[category])
                if equipped != None:
                    if equipped == 'Fist':
                        pass
                    else:
                        print(f"You unequipped {equipped}.")
                        backpack.pick_item(equipped, 1)
                    self.max_health   -= equippable[category][equipped].max_health
                    self.attack       -= equippable[category][equipped].attack
                    self.max_attack   -= equippable[category][equipped].max_attack
                    self.crit         -= equippable[category][equipped].crit
                    self.attack_speed -= equippable[category][equipped].attack_speed
                    self.armour       -= equippable[category][equipped].armour              
                equipped = item
                if equipped == 'Fist':
                    pass
                else:
                    print(f"You equiped {equipped}.")
                    backpack.delete_item(equipped, 1)
                self.max_health     += equippable[category][item].max_health
                self.attack         += equippable[category][item].attack
                self.max_attack     += equippable[category][item].max_attack
                self.crit           += equippable[category][item].crit
                self.attack_speed   += equippable[category][item].attack_speed
                self.armour         += equippable[category][item].armour
                setattr(self, slots[category], item)

slots = {
    'Weapons': 'equipped_weapon',
    'Armour': 'equipped_armour',
    'Headwear': 'equipped_headwear',
    'Rings': 'equipped_ring'
}

xp_drop = {
    'low':      (30, 50),
    'mid':      (80, 110),
    'high':     (180, 230),
    'elite':    (500, 900),
}

stat_upgrades = {
    '1': ('max_health', 5),
    '2': ('attack', 1),
    '3': ('armour', 1),
}

if __name__ == "__main__":
    player = Character()

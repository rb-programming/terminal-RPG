class Bonus:
    def __init__(self, max_health=0, attack=0, max_attack = 0, crit=0, attack_speed=0, armour=0):
        self.max_health = max_health    
        self.attack = attack
        self.max_attack = max_attack
        self.crit = crit
        self.attack_speed = attack_speed
        self.armour = armour

def equipment_available(backpack):
    bonuses = {}
    for category in equippable:
        for item in equippable[category]:
            if item in backpack.itemdict and backpack.itemdict[item] != 0:
                bonuses["Max health"] = equippable[category][item].max_health
                bonuses["Attack"] = equippable[category][item].attack
                bonuses["Max attack"] = equippable[category][item].max_attack
                bonuses["Crit"] = equippable[category][item].crit
                bonuses["Attack speed"] = equippable[category][item].attack_speed
                bonuses["Armour"] = equippable[category][item].armour
                stats = [f"+{amount} {stat}" for stat, amount in bonuses.items()
                        if amount != 0]
                print(f"{item} | {', '.join(stats)}")

equippable = {
    "Weapons": {
        "Fist":          Bonus(),
        "Bow":           Bonus(attack=6,  max_attack=10,  attack_speed=0.25),
        "Spear":         Bonus(attack=4,  max_attack=5),
        "Dagger":        Bonus(attack=1,  max_attack=2,  attack_speed=0.45, crit=0.05),
        "Iron Sword":    Bonus(attack=6,  max_attack=8),
        "Steel Sword":   Bonus(attack=10, max_attack=13),
        "War Hammer":    Bonus(attack=16, max_attack=20, attack_speed=-0.2, crit=0.05),
        "Dragon Slayer": Bonus(attack=22, max_attack=28, attack_speed=0.1,  crit=0.1),
    },
 
    "Armour": {
        "Cloth Armour":   Bonus(max_health=8,  armour=2),
        "Leather Armour": Bonus(max_health=16, armour=4),
        "Iron Armour":    Bonus(max_health=26, armour=7),
        "Steel Armour":   Bonus(max_health=40, armour=11),
        "Dragon Armour":  Bonus(max_health=60, armour=16),
    },
 
    "Headwear": {
        "Cloth Hood":   Bonus(max_health=5,  armour=1),
        "Leather Cap":  Bonus(max_health=9,  armour=2),
        "Iron Helmet":  Bonus(max_health=14, armour=4),
        "Steel Helmet": Bonus(max_health=20, armour=6,  crit=0.03),
        "Dragon Helm":  Bonus(max_health=30, armour=9,  crit=0.06),
    },
 
    "Rings": {
        "Bone Ring":     Bonus(crit=0.03),
        "Spider Ring":   Bonus(attack_speed=0.15, crit=0.02),
        "Iron Ring":     Bonus(attack=2, max_attack=2),
        "Steel Ring":    Bonus(attack=4, max_attack=4, crit=0.02),
        "Emerald Ring":  Bonus(max_health=20),
        "Ruby Ring":     Bonus(attack=6, max_attack=7),
        "Sapphire Ring": Bonus(attack_speed=0.2),
        "Diamond Ring":  Bonus(crit=0.1),
        "Dragon Ring":   Bonus(attack=7, max_attack=9, attack_speed=0.15, crit=0.05),
    },
}


if __name__ == '__main__':
    import inventory
    backpack = inventory.Inventory()
    backpack.pick_item("Stick", 1)
    backpack.pick_item("Bow", 1)
    backpack.pick_item("Cloth Armour", 1)
    equipment_available(backpack)
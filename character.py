import random

class Character:
    def __init__(self, name, current_health = 100, max_health = 100, attack = 9, max_attack = 14, armour = 5, xp = 0, level = 1):
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.attack = attack
        self.max_attack = max_attack
        self.armour = armour
        self.level = level
        self.xp = xp

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

xp_drop = {
    'low': (30, 50),
    'mid': (80, 110),
    'high': (180, 230),
    'elite': (500, 900),
}

stat_upgrades = {
    '1': ('max_health', 5),
    '2': ('attack', 1),
    '3': ('max_attack', 2),
    '4': ('armour', 1),
}
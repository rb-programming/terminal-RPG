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

    def gain_xp(self, difficulty):
        if difficulty == 'low':
            self.xp += random.randint(30, 50)
        if difficulty == 'mid':
            self.xp += random.randint(60, 90)
        if difficulty == 'high':
            self.xp += random.randint(100, 150)
        if difficulty == 'elite':
            self.xp += int(75 * self.level ** 1.6 * 2)

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
class Character:
    def __init__(self, name, health = 100, max_health = 100, attack = 9, max_attack = 14, armour = 5, xp = 0, level = 1):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.max_attack = max_attack
        self.armour = armour
        self.level = level
        self.xp = xp

    def greeting(self):
        print(f"Good luck on your journey, {self.name}!")

    def level_up(self):
        if self.xp >= 75 * self.level ** 1.6:
            self.xp -= 75 * self.level ** 1.6
            self.level += 1
        else:
            print(f"Farm more.\nYou have {int(self.xp)}/{int(75 * self.level ** 1.6)} xp.")

    def gain_xp(self, amount):
        self.xp += amount

    def get_damaged(self, amount):
        self.health -= amount

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True


if __name__ == "__main__":
    my_character = Character("Victor(y)", 1, 7, 5)
    my_character.gain_xp(500)
    my_character.level_up()
    my_character.level_up()
    my_character.level_up()
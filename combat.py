import enemy
import character
import random
import time

difficulties = {
    "low": enemy.low,
    "mid": enemy.mid,
    "high": enemy.high,
    "elite": enemy.elite,
}

def choose_enemy(difficulty):
    return random.choice(difficulties[difficulty])

def start_combat(player, nemesis):
    player.health = player.max_health
    nemesis.health = 100
    print(f"You are fighting a {nemesis.name}")

def calculate_damage(attacker, defender):
    damage = random.randint(attacker.attack, attacker.max_attack)
    final_damage = damage * (100 / (100 + defender.armour * 10))
    return(final_damage)

def switch_turn(turn):
    if turn == "player":
        return "enemy"
    else:
        return "player"
    
def drop_items():
    pass



if __name__ == "__main__":
    my_character = character.Character("John")
    nemesis = choose_enemy(input("Choose between difficulties\nlow / mid / high / elite: "))
    start_combat(my_character, nemesis)
    turn = "player"
    while my_character.is_alive() and nemesis.is_alive():
        if turn == "player":
            input("Press 'Enter' to hit the enemy.")
            damage = calculate_damage(my_character, nemesis)
            nemesis.health -= damage
            if nemesis.health > 0:
                print(f"You dealt {int(damage)} damage and the enemy has {int(nemesis.health)} hp remaining.")
            else:
                print("The enemy has been slain, you are victorious!")
            turn = switch_turn("player")
        else:
            time.sleep(0.5)
            damage = calculate_damage(nemesis, my_character)
            my_character.health -= calculate_damage(nemesis, my_character)
            if my_character.health > 0:
                print(f"The enemy dealt {int(damage)} and you have {int(my_character.health)} hp remaining.")
            else:
                print("You died.")
            turn = switch_turn("enemy")
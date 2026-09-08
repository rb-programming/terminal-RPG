import enemy
import character
import random
import time
import inventory
from colored import Fore, Style

difficulties = {
    "low": enemy.low,
    "mid": enemy.mid,
    "high": enemy.high,
    "elite": enemy.elite,
}

def choose_enemy(difficulty):
    return random.choice(difficulties[difficulty])

def start_combat(player, nemesis):
    player.current_health = player.max_health
    nemesis.current_health = nemesis.current_health
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
    player = character.Character("John")
    backpack = inventory.Inventory()
    while player.is_alive():
        nemesis = choose_enemy(input("Choose between difficulties\nlow / mid / high / elite: "))
        start_combat(player, nemesis)
        turn = "player"
        while player.is_alive() and nemesis.is_alive():
            if turn == "player":
                input(f"Press {Fore.yellow}'Enter'{Style.reset} to hit the enemy.")
                damage = calculate_damage(player, nemesis)
                nemesis.current_health -= damage
                if nemesis.current_health > 0:
                    print(f"You dealt {Fore.green}{int(damage)}{Style.reset} damage and the enemy has {Fore.red}{int(nemesis.current_health)}{Style.reset} hp remaining.")
                else:
                    print("The enemy has been slain, you are victorious!")
                turn = switch_turn("player")
            else:
                time.sleep(0.5)
                damage = calculate_damage(nemesis, player)
                player.current_health -= calculate_damage(nemesis, player)
                if player.current_health > 0:
                    print(f"The enemy dealt {Fore.red}{int(damage)}{Style.reset} and you have {Fore.green}{int(player.current_health)}{Style.reset} hp remaining.")
                else:
                    print("You died.")
                turn = switch_turn("enemy")
        if player.is_alive():
            for drops in nemesis.drops:
                rate = random.random()
                if rate <= drops.drop_rate:
                    amount = (random.randint(drops.min_amount, drops.max_amount))
                    backpack.pick_item(item=drops.item, amount=amount)
        backpack.show_inventory()
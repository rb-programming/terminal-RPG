import enemy
import random
import time
import math
import ui

from ui import reset, bold, green, yellow, magenta, red

difficulties = {
    "low": enemy.low,
    "mid": enemy.mid,
    "high": enemy.high,
    "elite": enemy.elite,
}

def choose_enemy(difficulty):
    return random.choice(difficulties[difficulty])

def calculate_damage(attacker, defender):
    damage = random.randint(attacker.attack, attacker.max_attack)
    final_damage = damage * (100 / (100 + defender.armour * 10))
    return final_damage


def fight(player, backpack, difficulty):
    enemy = choose_enemy(difficulty)
    player.current_health = player.max_health
    enemy.current_health = enemy.max_health
    ui.refresh(player)
    ui.enemy(enemy, difficulty)
    turn = "player"
    log = []
    attack_remainder = 0
    while player.is_alive() and enemy.is_alive():
        ui.refresh(player)
        ui.enemy(enemy, difficulty)
        for i in log:
            print(i)
        if turn == "player":
            time.sleep(0.5)
            attack_remainder += player.attack_speed
            if attack_remainder >= 1:
                if math.isclose(attack_remainder, 2):
                    attack_remainder = round(attack_remainder, 0)
                for i in range(int(attack_remainder)):
                    crit = False
                    crit_chance = random.random()
                    attack_remainder -= 1.0
                    if player.crit < crit_chance:
                        damage = calculate_damage(player, enemy)
                    else:
                        damage = calculate_damage(player, enemy) * 1.5
                        crit = True
                    enemy.get_damaged(damage)
                    if enemy.current_health > 0:
                        if crit:
                            hit_message = f"{magenta + bold}{player.name}{reset} hits {magenta + bold}{enemy.name}{reset} with {yellow}all of his might{reset} for {red + bold}{int(damage)}{reset} damage."
                        else:
                            hit_message = f"{magenta + bold}{player.name}{reset} hits {magenta + bold}{enemy.name}{reset} for {red + bold}{int(damage)}{reset} damage."
                        log.append(hit_message)
                    else:
                        log.append(f"You have slain the {red + (enemy.name).lower() + reset}!")
                        break
            turn = 'enemy'
        else:
            time.sleep(0.5)
            damage = calculate_damage(enemy, player)
            player.get_damaged(damage)
            if player.current_health > 0:
                hit_message = f"{magenta + bold}{enemy.name}{reset} hits {magenta + bold}{player.name}{reset} for {red + bold}{int(damage)}{reset} damage."
                log.append(hit_message)
                print(hit_message)
            else:
                log.append(f"{red}You {bold}DIED!{reset}")
                print(f"{red}You {bold}DIED!{reset}")
            turn = 'player'
    ui.refresh(player)
    ui.enemy(enemy, difficulty)
    for i in log:
        print(i)
    if player.is_alive():
        player.gain_xp(difficulty)
        for drops in enemy.drops:
            rate = random.random()
            if rate <= drops.drop_rate:
                amount = (random.randint(drops.min_amount, drops.max_amount))
                backpack.pick_item(item=drops.item, amount=amount)
                print(f"{green}+{amount}{reset} {drops.item}")
        time.sleep(2)
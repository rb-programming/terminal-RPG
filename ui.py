from colored import Fore, Style
import os

bold = '\33[1m'
green = Fore.green
red = Fore.red
blue = Fore.blue
yellow = Fore.yellow
magenta = Fore.magenta

reset = Style.reset

clear_terminal = os.system('cls' if os.name == 'nt' else 'clear')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def refresh(player):
    clear_terminal()
    topbar(player)

def output(*args):
    sep = f'\n{'='*70}'
    for i in args:
        print(i, sep, end='\n')

def topbar(player):
    output(f"{blue + bold}Terminal RPG{reset}",
      f"{green + bold}Player{reset}: {green}{player.name}{reset} \t\tHP: {green}{int(player.current_health)}{reset}/{player.max_health}\tXP: {green}{player.xp}{reset}/{int(75 * player.level ** 1.6)}\tLevel: {green + bold}{player.level}{reset}"
      )

def enemy(enemy, difficulty):
    output(f"{red + bold}Enemy{reset}: {red}{enemy.name}{reset} ({difficulty}) \tHP: {red}{int(enemy.current_health)}{reset}/{enemy.max_health}")
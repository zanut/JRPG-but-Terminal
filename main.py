import os
import random
import sys
import csv

from Equipment import Equipment
from Player import Player
from Skill import Skill
from playerdata import PlayerData
from Monster import Monster
from Mechanical import Mechanical

SKILL = []
with open('skill_name.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        SKILL.append(r)

SKILL = [Skill(key['base_power'],
               key['dmg_multiplier'],
               key['mp_cost'],
               key['upgraded_lv'],
               key['name'])for key in SKILL]

def generate_monster(l):
    leval_monster = random.randint(l-1, l+1)
    rand_mons = Monster(lv=leval_monster)
    for _ in range(random.randint(1, 3)):
        rand_mons.skill(SKILL[random.randint(0, len(SKILL)-1)])
    return rand_mons


while True:
    os.system('clear')
    print('JRPG but Terminal')
    print('1. New Game\n2. Load Game\n3. Exit')
    choice = input('Choice: ')
    if choice == '1':
        player = Player(lv=1,
                        weapon=Equipment(10, 1.5, 0),
                        armor=Equipment(10, 1.5, 0),
                        skill=[Skill(10, 1.5, 10, 0, 'Slash')],
                        name=input('Name: '),
                        )
        break
    elif choice == '2':
        name = PlayerData().all_name()
        if len(name) > 0:
            for i in range(len(name)):
                print(f"{i + 1}. {name[i]}")
            while True:
                player = None
                choice = input("Choice(any letter to quit): ")
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(name):
                        player = PlayerData().load(name[choice - 1])
                        break
                    else:
                        print("Invalid choice please try again")
                else:
                    break
            if player:
                break
        else:
            print('Save is empty')
    elif choice == '3':
        sys.exit()
    else:
        print('Invalid choice')
in_game = Mechanical(player)
in_game.after_game()
while True:
    choice = input("Wanna fight (y/n): ")
    if choice == 'y':
        monster = generate_monster(in_game.player.lv)
        result = in_game.fight(monster)
        if result:
            in_game.player.lv_up()
        in_game.player.restore()
    elif choice == 'n':
        in_game.after_game()



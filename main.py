import os
import random
import sys

from Equipment import Equipment
from Player import Player
from Skill import Skill
from playerdata import PlayerData
from Monster import Monster
from Mechanical import Mechanical


def generate_monster(l):
    leval_monster = random.randint(l-1, l+1)
    monster = Monster(lv=leval_monster)
    return monster


while True:
    os.system('cls')
    print('JRPG but Terminal')
    print('1. New Game\n2. Load Game\n3. Exit')
    choice = input('Choice: ')
    if choice == '1':
        player = Player(lv=1,
                        weapon=Equipment(10, 1.5, 0),
                        armor=Equipment(10, 1.5, 0),
                        skill=Skill(10, 1.5, 10, 0, 'Slash'),
                        name=input('Name: '),
                        )
        break
    elif choice == '2':
        name = PlayerData().all_name()
        if len(name) > 0:
            for i in range(len(name)):
                print(f"{i + 1}. {name[i]}")
            while True:
                choice = input("Choice(any letter to quit): ")
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(name):
                        player = PlayerData().load(name[choice - 1])
                        break
                    else:
                        print("Invalid choice")
                else:
                    break
            break
        else:
            print('Empty save')
    elif choice == '3':
        sys.exit()
    else:
        print('Invalid choice')
in_game = Mechanical(player)
while True:
    choice = input("Continue? (y/n): ")
    if choice == 'y':
        monster = generate_monster(in_game.player.lv)
        result = in_game.fight(monster)
        if result:
            if in_game.player.lv_up():
                continue
        in_game.player.restore()
    elif choice == 'n':
        in_game.after_game()



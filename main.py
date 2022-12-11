import os
import random
import sys
import time

from Equipment import Equipment
from Player import Player
from Skill import Skill
from playerdata import PlayerData
from Mechanical import Mechanical
from tools import generate_monster, print_withtime, print_withspace

# menu system part
while True:
    os.system('clear')
    print_withspace('=' * 40)
    print_withspace('.......... Welcome to the game .........')
    print_withspace('=' * 40)
    print_withspace('........... JRPG but Terminal ..........')
    print_withspace('=' * 40)
    print_withspace('1. New Game\n2. Load Game\n3. Exit')
    print_withspace('=' * 40)
    print_withtime('Choice: ')
    choice = input()
    if choice == '1':
        # New Game default setup
        player = Player(lv=1,
                        weapon=Equipment(15, 1.3, 0, base='Sword'),
                        armor=Equipment(15, 1.3, 0, base='Armor'),
                        skill=[Skill(25, 1.5, 10, 0, 'Slash')],
                        name=input('Name: '),
                        )
        print_withspace(f'Welcome to the game {player.name}')
        time.sleep(1)
        break
    elif choice == '2':
        # Load Game
        time.sleep(1)
        name = PlayerData().all_name()
        if len(name) > 0:
            os.system('clear')
            print_withspace('Saved game: ')
            print_withspace('=' * 40)
            for i in range(len(name)):
                print_withspace(f"{i + 1}. {name[i]}")
            print_withspace('=' * 40)
            while True:
                player = None
                print_withtime("Choice(any letter to quit): ")
                choice = input()
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(name):
                        player = PlayerData().load(name[choice - 1])
                        break
                    else:
                        print_withspace("Invalid choice please try again")
                else:
                    break
            if player:
                break
        else:
            print_withspace('Save is empty')
            time.sleep(1)
    elif choice == '3':
        # Exit
        print_withspace(f'Game is closing . . .')
        time.sleep(0.5)
        sys.exit()
    else:
        print_withspace('Invalid choice please try again')

# Game loop part
in_game = Mechanical(player)
in_game.after_game()
while True:
    in_game.player.restore()
    print_withtime("Wanna fight (y/n): ")
    choice = input()
    picture = random.randint(0, 3)  # random monster picture
    if choice == 'y':
        # fight part
        monster = generate_monster(in_game.player.lv, PlayerData().read_skill('skill_name.csv'))
        result = in_game.fight(monster, picture)
        if result:  # if player win
            in_game.player.lv_up(PlayerData().read_skill('skill_name.csv'))
        elif not result:  # if player lose or run
            in_game.after_game()  # back to base
    elif choice == 'n':
        in_game.after_game()  # back to base

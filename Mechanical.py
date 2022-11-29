import os
import sys
import time
import Ascii_model


from Monster import Monster
from Player import Player
from Equipment import Equipment
from Skill import Skill
from playerdata import PlayerData
from tools import print_withtime, print_withspace


class Mechanical:
    def __init__(self, player: Player):
        self.player = player

    def load_game(self):
        name = PlayerData(self.player.name).all_name()
        if len(name) > 0:
            while True:
                os.system('clear')
                print_withspace('Loaded game:')
                print_withspace('=' * 40)
                for i in range(len(name)):
                    print_withspace(f"{i + 1}. {name[i]}")
                print_withspace('=' * 40)
                print_withtime("Choice(any letter to quit): ")
                choice = input()
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(name):
                        self.player = PlayerData(self.player.name).load(
                            name[choice - 1])
                        print_withspace(f"Loaded {name[choice - 1]}")
                        break
                    else:
                        print_withspace("Invalid choice")
                else:
                    break
        else:
            print_withspace("Save is empty")

    def stat_up(self):
        while True:
            os.system('clear')
            print('=' * 75)
            for key, value in self.player.stat.items():
                print_withspace(f"{key}: {value}")
            print('=' * 75)
            print_withspace(f"Point: {self.player.point}")
            print('=' * 75)
            print_withtime("Point you want to spend (any letter to quit): ")
            consume = input()
            if consume.isdigit():
                consume = int(consume)
                if consume > self.player.point:
                    print_withspace("Not enough point")
                else:
                    print_withtime("Stat you want to upgrade: ")
                    stat = input()
                    if stat in self.player.stat:  # Check if stat is in dict
                        self.player.point -= consume
                        self.player.stat[stat] += consume
                    else:
                        print_withspace("Invalid stat")
            else:
                break

    def upgrade_equipment(self, equipment: Equipment):
        if self.player.gold < equipment.cost_upgrade:
            print_withspace(f"Not enough gold you need {equipment.cost_upgrade - self.player.gold}")
        else:
            self.player.gold -= equipment.cost_upgrade
            equipment.upgrade()
            print_withspace(f"Weapon upgraded Gold left: {self.player.gold}")

    def upgrade_skill(self, skill: [Skill]):
        if isinstance(skill, list) and len(skill) > 0:
            print('=' * 75)
            for i in range(len(self.player.skill)):
                print_withspace(f"{i + 1}. {self.player.skill[i].name} ({self.player.skill[i].cost_upgrade} Gold)")
            print('=' * 75)
            while True:
                choice = input("Choice(any letter to quit): ")
                if choice.isdigit() and 0 < int(choice) <= len(self.player.skill):
                    if self.player.gold < self.player.skill[int(choice) - 1].cost_upgrade:
                        print_withspace("Not enough gold")
                    else:
                        self.player.gold -= self.player.skill[
                            int(choice) - 1].cost_upgrade
                        self.player.skill[int(choice) - 1].upgrade()
                        print_withspace(f"Skill upgraded Gold left: {self.player.gold}")
                elif choice.isdigit():
                    print_withspace("Incorrect choice")
                else:
                    break

    def used_skill(self, monster: Monster):
        if len(self.player.skill) > 0:
            while True:
                print('=' * 75)
                for i in range(len(self.player.skill)):
                    print(f"{i + 1}. {self.player.skill[i].name}")
                print('=' * 75)
                choice = input("Choice(any letter to quit): ")
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(self.player.skill):
                        if self.player.skill[choice - 1].mp_cost <= self.player.mp:
                            self.player.mp -= self.player.skill[choice - 1].mp_cost
                            monster.hp -= self.player.skill[choice - 1].dmg()
                            break
                        else:
                            print("Not enough MP")
                            continue
                    else:
                        print("Incorrect choice")
                else:
                    break

    def after_game(self):
        while True:
            os.system('clear')
            print('=' * 75)
            print_withtime(f"Gold: {self.player.gold} ")
            print_withspace(f"Exp: {self.player.exp_required[0]}/{self.player.exp_required[1]}")
            print('=' * 75)
            print_withspace('1. Upgrade\n2. Stats\n3. Save\n4. Load\n5. Leave base\n6. Exit Game ')
            print('=' * 75)
            choice = input("Choice: ")
            if choice == '1':
                while True:
                    os.system('clear')
                    print('=' * 75)
                    print_withspace(f'Gold: {self.player.gold}')
                    print('=' * 75)
                    print_withspace(f"1. Weapon ({self.player.weapon.cost_upgrade} Gold)\n"
                          f"2. Armor ({self.player.armor.cost_upgrade} Gold)\n"
                          f"3. Skill\n"
                          f"4. Exit")
                    print('=' * 75)
                    choice = input("Choice: ")
                    if choice == '1':
                        self.upgrade_equipment(self.player.weapon)
                        time.sleep(1)
                        os.system('clear')
                        continue
                    elif choice == '2':
                        self.upgrade_equipment(self.player.armor)
                        time.sleep(1)
                        os.system('clear')
                        continue
                    elif choice == '3':
                        self.upgrade_skill(self.player.skill)
                        time.sleep(1)
                        os.system('clear')
                        continue
                    elif choice == '4':
                        break
                    else:
                        print_withspace("Invalid choice")
            elif choice == '2':
                self.stat_up()
            elif choice == '3':
                PlayerData(self.player.name).save(self.player)
                print_withspace("Game saved")
                time.sleep(1)
            elif choice == '4':
                self.load_game()
            elif choice == '5':
                break
            elif choice == '6':
                print_withspace("Game closing ...")
                time.sleep(1)
                return sys.exit()

    def fight(self, monster: Monster, picture: int):
        while True:
            os.system('clear')
            print('=' * 75)
            print(f"Monster HP: {monster.hp}", end=' ')
            print(f'Monster MP: {monster.mp}')
            print('=' * 75)
            print(f'{Ascii_model.monster()[picture]}')
            print('=' * 75)
            print_withtime(f"Player HP: {self.player.hp} ")
            print_withtime(f"MP: {self.player.mp} ")
            print_withtime(f"Atk: {self.player.power(self.player.weapon)} ")
            print_withspace(f"Def: {self.player.power(self.player.armor)}")
            print('=' * 75)
            print_withspace("1. Attack\n2. Skill\n3. Run")
            print('=' * 75)
            print_withtime("Choice: ")
            choice = input()
            if choice == '1':
                monster.hp -= self.player.power(self.player.weapon)
                print_withspace(f"Player attack {self.player.power(self.player.weapon)}")
                time.sleep(1)
            elif choice == '2':
                self.used_skill(monster)
            elif choice == '3':
                print_withspace("You run away")
                return None
            if monster.hp <= 0:
                gold = monster.gold
                xp = monster.xp
                os.system('clear')
                print_withspace("You win")
                print_withspace(f"You received {gold} gold")
                print_withspace(f"You received {xp} exp")
                self.player.exp_required[0] += xp
                self.player.gold += gold
                return True
            dmg_received = monster.action() - self.player.power(self.player.armor)
            if dmg_received > 0:
                self.player.hp -= dmg_received
                print_withspace(f"You received {dmg_received} damage")
                time.sleep(1)
            elif dmg_received < 0:
                self.player.hp -= 1
                print_withspace(f"You received 1 damage")
                time.sleep(1)
            if self.player.hp <= 0:
                print_withspace("You lose")
                return False

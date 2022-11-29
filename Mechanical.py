import os
import sys
import time

from Monster import Monster
from Player import Player
from Equipment import Equipment
from Skill import Skill
from playerdata import PlayerData
import Ascii_model

class Mechanical:
    def __init__(self, player: Player):
        self.player = player

    def load_game(self):
        name = PlayerData(self.player.name).all_name()
        if len(name) > 0:
            while True:
                os.system('clear')
                for i in range(len(name)):
                    print(f"{i + 1}. {name[i]}")
                choice = input("Choice(any letter to quit): ")
                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(name):
                        self.player = PlayerData(self.player.name).load(
                            name[choice - 1])
                        break
                    else:
                        print("Invalid choice")
                else:
                    break
        else:
            print("Save is empty")

    def stat_up(self):
        while True:
            os.system('clear')
            for key, value in self.player.stat.items():
                print(f"{key}: {value}")
            print(f"Point: {self.player.point}")
            consume = input("Point you want to use (any letter to quit): ")
            if consume.isdigit():
                consume = int(consume)
                if consume > self.player.point:
                    print("Not enough point")
                else:
                    self.player.point -= consume
                    stat = input("Stat you want to upgrade: ")
                    if stat in self.player.stat:  # Check if stat is in dict
                        self.player.stat[stat] += consume
            else:
                break

    def upgrade_equipment(self, equipment: Equipment):
        if self.player.gold < equipment.cost_upgrade:
            print(f"Not enough gold you need {equipment.cost_upgrade - self.player.gold}")
        else:
            self.player.gold -= equipment.cost_upgrade
            equipment.upgrade()
            print(f"Weapon upgraded Gold left: {self.player.gold}")

    def upgrade_skill(self, skill: [Skill]):
        if isinstance(skill, list) and len(skill) > 0:
            for i in range(len(self.player.skill)):
                print(f"{i + 1}. {self.player.skill[i].name}")
            choice = input("Choice: ")
            if self.player.gold < self.player.skill[int(choice) - 1].cost_upgrade:
                print("Not enough gold")
            else:
                self.player.gold -= self.player.skill[
                    int(choice) - 1].cost_upgrade
                self.player.skill[int(choice) - 1].upgrade()
                print(f"Skill upgraded Gold left: {self.player.gold}")

    def used_skill(self, monster: Monster):
        if len(self.player.skill) > 0:
            while True:
                os.system('clear')
                for i in range(len(self.player.skill)):
                    print(f"{i + 1}. {self.player.skill[i].name}")
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
            print(f"Gold: {self.player.gold}", end=' ')
            print(f"Exp: {self.player.exp_required[0]}/{self.player.exp_required[1]}")
            print('1. Upgrade\n2. Stats\n3. Save\n4. Load\n5. Leave base\n6. Exit Game ')
            choice = input("Choice: ")
            if choice == '1':
                while True:
                    print("1. Weapon\n2. Armor\n3. Skill\n4. Exit")
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
                        print("Invalid choice")
            elif choice == '2':
                self.stat_up()
            elif choice == '3':
                PlayerData(self.player.name).save(self.player)
            elif choice == '4':
                self.load_game()
            elif choice == '5':
                break
            elif choice == '6':
                print("Game closing ...")
                return sys.exit()

    def fight(self, monster: Monster, picture: int):
        while True:
            os.system('clear')
            print(f"Monster HP: {monster.hp}")
            print(f'{Ascii_model.monster()[picture]}')
            print(f"Player HP: {self.player.hp}")
            print("1. Attack\n2. Skill\n3. Run")
            choice = input("Choice: ")
            if choice == '1':
                monster.hp -= self.player.weapon.get_power() + (self.player.stat['str']*0.5)
            elif choice == '2':
                self.used_skill(monster)
            elif choice == '3':
                print("You run away")
                return None
            if monster.hp <= 0:
                os.system('clear')
                print("You win")
                self.player.exp_required[0] += monster.xp
                self.player.gold += monster.gold
                return True
            monster_dmg = monster.action()
            print(monster_dmg)
            dmg_received = monster_dmg - (self.player.armor.get_power() + (self.player.stat['vit'] * 0.5))
            if dmg_received > 0:
                self.player.hp -= dmg_received
                print(f"You received {dmg_received} damage")
            elif dmg_received < 0:
                self.player.hp -= 1
                print(f"You received 1 damage")
            if self.player.hp <= 0:
                print("You lose")
                return False

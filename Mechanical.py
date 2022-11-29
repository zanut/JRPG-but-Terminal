import os
import sys

from Monster import Monster
from Player import Player
from Equipment import Equipment
from Skill import Skill
from playerdata import PlayerData


class Mechanical:
    def __init__(self, player: Player):
        self.player = player

    def fight(self, monster: Monster):
        while True:
            print("1. Attack\n2. Skill\n3. Run")
            choice = input("Choice: ")
            if choice == '1':
                monster.hp -= self.player.weapon.get_power() + (self.player.stat['str']*0.5)
            elif choice == '2':
                if len(self.player.skill) > 0:
                    for i in range(len(self.player.skill)):
                        print(f"{i + 1}. {self.player.skill[i].name}")
                    choice = input("Choice: ")
                    monster.hp -= self.player.skill[int(choice) - 1].get_power()
                # if self.player.skill.mp_cost > self.player.mp:
                #     print("Not enough mana")
                # else:
                #     self.player.mp -= self.player.skill.mp_cost
                #     monster.hp -= self.player.skill.get_power()
            elif choice == '3':
                print("You run away")
                return None
            if monster.hp <= 0:
                print("You win")
                self.player.exp_required[0] += monster.xp
                self.player.gold += monster.gold
                return True
            self.player.hp -= monster.atk - self.player.armor.get_power() - (
                        self.player.stat['vit'] * 0.5)
            if self.player.hp <= 0:
                print("You lose")
                return False

    def after_game(self):
        while True:
            print('1. Upgrade\n2. Stats\n3. Save\n4. Load\n5. Exit')
            choice = input("Choice: ")
            if choice == '1':
                while True:
                    print("1. Weapon\n2. Armor\n3. Skill\n4. Exit")
                    choice = input("Choice: ")
                    if choice == '1':
                        self.upgrade_equipment(self.player.weapon)
                        os.system('cls')
                        continue
                    elif choice == '2':
                        self.upgrade_equipment(self.player.armor)
                        os.system('cls')
                        continue
                    elif choice == '3':
                        self.upgrade_skill(self.player.skill)
                        os.system('cls')
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
                print("Game closing ...")
                return sys.exit()

    def load_game(self):
        name = PlayerData(self.player.name).all_name()
        if len(name) > 0:
            for i in range(len(name)):
                print(f"{i + 1}. {name[i]}")
            while True:
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

    def stat_up(self):
        for key, value in self.player.stat.items():
            print(f"{key}: {value}")
        print(f"Point: {self.player.point}")
        while True:
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
            print(
                f"Not enough gold you need {equipment.cost_upgrade - self.player.gold}")
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

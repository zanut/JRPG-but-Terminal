import sys

from Monster import Monster
from Player import Player
from Equipment import Equipment
from Skill import Skill

class Mechanical:
    def __init__(self, player: Player):
        self.player = player

    def fight(self, monster: Monster):
        while True:
            print("1. Attack\n2. Skill\n3. Run")
            choice = input("Choice: ")
            if choice == '1':
                monster.hp -= self.player.weapon.get_power() + (self.player.stat['str']*0.5)
                if monster.hp <= 0:
                    print("You win")
                    self.player.exp_required[0] += monster.xp
                    self.player.lv_up()
                    self.player.gold += monster.gold
                self.player.hp -= monster.atk - self.player.armor.get_power() - (self.player.stat['vit']*0.5)
                if self.player.hp <= 0:
                    print("You lose")
                    return self.after_game()
            elif choice == '2':
                if self.player.skill.mp_cost > self.player.mp:
                    print("Not enough mana")
                else:
                    self.player.mp -= self.player.skill.mp_cost
                    monster.hp -= self.player.skill.dmg()
                    if monster.hp <= 0:
                        print("You win")
                        self.player.exp_required[0] += monster.xp
                        self.player.lv_up()
                        self.player.gold += monster.gold
                        return self.after_game()
                    self.player.hp -= monster.atk - self.player.armor.get_power() - (self.player.stat['vit']*0.5)
                    if self.player.hp <= 0:
                        print("You lose")
                        return self.after_game()
            elif choice == '3':
                print("You run")
                return self.after_game()

    def after_game(self):
        while True:
            print('1. Upgrade\n2. Stats\n3. Save\n 4. Load\n5. Exit')
            choice = input("Choice: ")
            if choice == '1':
                print("1. Weapon\n2. Armor\n3. Skill")
                choice = input("Choice: ")
                if choice == '1':
                    if self.player.gold < self.player.weapon.cost_upgrade:
                        print("Not enough gold")
                    else:
                        self.player.gold -= self.player.weapon.cost_upgrade
                        self.player.weapon.upgrade()
                elif choice == '2':
                    if self.player.gold < self.player.armor.cost_upgrade:
                        print("Not enough gold")
                    else:
                        self.player.gold -= self.player.armor.cost_upgrade
                        self.player.armor.upgrade()
                elif choice == '3':
                    if self.player.gold < self.player.skill.cost_upgrade:
                        print("Not enough gold")
                    else:
                        self.player.gold -= self.player.skill.cost_upgrade
                        self.player.skill.upgrade()
            elif choice == '2':
                for key, value in self.player.stat.items():
                    print(f"{key}: {value}")
                print(f"Point: {self.player.point}")
            elif choice == '3':
                self.save() # save game to json file maybe ?
            elif choice == '4':
                self.load() # load game
            elif choice == '5':
                return sys.exit()

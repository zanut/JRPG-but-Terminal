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
                    monster.hp -= self.player.skill.dmg()
                    if monster.hp <= 0:
                        print("You win")
                        self.player.exp_required[0] += monster.xp
                        self.player.lv_up()
                        self.player.gold += monster.gold
                        return self.after_game()
                    self.player.hp -= monster.atk - self.player.armor.get_power() - self.player.stat['vit']
                    if self.player.hp <= 0:
                        print("You lose")
                        return 0
            elif choice == '3':
                print("You run")
                return self.after_game()

    def after_game(self):
        while True:
            print('1. Upgrade\n2. Stats\n3. Save\n 4. Load\n5. Exit')

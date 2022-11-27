from Equipment import Equipment
from Skill import Skill


class Player:
    def __init__(self, lv: int, weapon: Equipment, armor: Equipment, skill: Skill, gold: int = 0):
        self.__hp = 100
        self.__lv = lv
        self.__weapon = weapon
        self.__armor = armor
        self.skill = skill
        self.stat = {'str': 5, 'int': 5, 'vit': 5}
        self.exp_required = [0, 100]  # [current exp, exp required to lv up]
        self.point = 0
        self._gold = gold

    def upgrade_stat(self, stat, value):
        self.stat[stat] += value

    def lv_up(self):
        if self.exp_required[0] > self.exp_required[1]:
            self.__lv += 1
            self.exp_required[0] -= self.exp_required[1]
            self.exp_required[1] += 100 * self.__lv
            self.point += 5

    @property
    def hp(self):
        return self.__hp + self.stat['vit'] * 10

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def weapon(self):
        return self.__weapon

    @property
    def armor(self):
        return self.__armor

    @property
    def lv(self):
        return self.__lv

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

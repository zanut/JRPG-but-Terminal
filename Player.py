from Equipment import Equipment
from Skill import Skill


class Player:
    def __init__(self, lv: int,
                 weapon: Equipment,
                 armor: Equipment,
                 skill: [Skill],
                 gold: int = 0,
                 name: str = 'Player',
                 xp: int = 0,
                 stat=None,
                 point: int = 0):
        if stat is None:
            stat = {'str': 5, 'vit': 5, 'int': 5}
        self._name = name
        self.__hp = 100
        self.__mp = 100
        self.__lv = lv
        self.__weapon = weapon
        self.__armor = armor
        self.skill = [skill]
        self.stat = stat
        self.exp_required = [xp, 100]  # [current exp, exp required to lv up]
        self.point = point
        self._gold = gold

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        hp = self.__hp + self.stat['vit'] * 10
        return hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def mp(self):
        mp = self.__mp + self.stat['int'] * 10
        return mp

    @mp.setter
    def mp(self, value):
        self.__mp = value

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

    def upgrade_stat(self, stat, value):
        self.stat[stat] += value

    def lv_up(self):
        if self.exp_required[0] > self.exp_required[1]:
            self.__lv += 1
            self.exp_required[0] -= self.exp_required[1]
            self.exp_required[1] += 100 * self.__lv
            self.point += 5

    def restore(self):
        self.hp = 100 + self.stat['vit'] * 10
        self.mp = 100 + self.stat['int'] * 10

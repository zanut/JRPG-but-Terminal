import random


class Monster:
    def __init__(self, lv, skill: Skill):
        self.__lv_mons = lv
        self.__skill = skill
        self._hp = 100 + lv * 20
        self._mp = 100 + lv * 5

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp = value

    @property
    def atk(self):
        return 5 * self.__lv_mons

    @property
    def dmg_reduction(self):
        return self.__lv_mons * 2

    @property
    def gold(self):
        return random.randint(100, 300) * self.__lv_mons

    @property
    def xp(self):
        return random.randint(150, 200) * self.__lv_mons

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    @property
    def lv(self):
        return self.__lv_mons

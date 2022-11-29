import random
from Skill import Skill


class Monster:
    def __init__(self, lv):
        self.__lv_mons = lv
        self._skill = []
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
    def lv(self):
        return self.__lv_mons

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill: Skill):
        self.skill.append(skill)

    def skill_used(self):
        index = random.randint(0, len(self.skill)-1)
        if self.skill[index].mp_cost > self.mp:
            power = self.skill[index].dmg
        else:
            power = self.atk
        return power

    def action(self):
        random_action = random.randint(0, 100)
        if random_action <= 60:
            return self.atk
        else:
            return self.skill_used()




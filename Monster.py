import random
from Skill import Skill


class Monster:
    def __init__(self, lv: int):
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
        self.skill.append(skill)  # add skill to the monster

    def skill_used(self):
        """ Return the damage from the skill used or attack if no skill is available """
        index = random.randint(0, len(self.skill)-1)
        if self.skill[index].mp_cost < self.mp:  # check if the monster have enough mp to use the skill
            self.mp -= self.skill[index].mp_cost
            power = self.skill[index].dmg()
            print(f'Monster used {self.skill[index].name}!')
        else:  # if the monster doesn't have enough mp to use the skill
            power = self.atk
            print('Monster used attack!')
        return power

    def action(self):
        """ making action for the monster which are attack or skill """
        random_action = random.randint(0, 100)
        if random_action <= 60:  # 60% chance to use normal attack
            return self.atk
        else:  # 40% chance to use skill
            return self.skill_used()

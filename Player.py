from Equipment import Equipment
from Skill import Skill
import tools


class Player:
    def __init__(self, lv: int,
                 weapon: Equipment,
                 armor: Equipment,
                 skill: list[Skill],
                 gold: int = 0,
                 name: str = 'Player',
                 xp: int = 0,
                 xp_need: int = 100,
                 stat=None,
                 point: int = 0):
        if stat is None:
            stat = {'str': 5, 'vit': 5, 'int': 5}
        self.__name = name
        self.__hp = 100 + stat['vit'] * 10
        self.__mp = 100 + stat['int'] * 10
        self.__lv = lv
        self.__weapon = weapon
        self.__armor = armor
        self.skill = skill
        self.stat = stat
        self.exp_required = [xp, xp_need]  # [current exp, exp required to lv up]
        self.point = point
        self.__gold = gold

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def mp(self):
        return self.__mp

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

    @lv.setter
    def lv(self, value):
        self.__lv = value

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value):
        self.__gold = value

    def upgrade_stat(self, stat, value):
        """ upgrade the stat of the player also part of the stat upgrade system """
        self.stat[stat] += value

    def lv_up(self, skill: [Skill]):
        """ level up the player and every 5 level up the player will get a new skill """
        while self.exp_required[0] > self.exp_required[1]:
            self.lv += 1
            self.exp_required[0] -= self.exp_required[1]
            self.exp_required[1] += 100 * self.lv
            self.point += 5
            print(f"Level up! You are now level {self.lv}!")
            print(f"You have {self.point} points to spend")
            if self.lv % 5 == 0:
                while True:
                    new_skill = tools.generate_skill(skill)
                    if new_skill.name in [s.name for s in self.skill]:
                        continue
                    else:
                        self.skill.append(new_skill)
                        print(f"You learned {new_skill.name}!")
                        break

    def restore(self):
        """ restore the hp and mp of the player to maximum """
        self.hp = 100 + self.stat['vit'] * 10
        self.mp = 100 + self.stat['int'] * 10

    def power(self, equip: Equipment):
        """ calculate the power of the player together from the weapon and armor """
        base = equip.get_power()
        if equip.base == 'Sword':
            return base + self.stat['str']*2
        elif equip.base == 'Armor':
            return base + self.stat['vit']*1.5

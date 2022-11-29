class Skill:
    def __init__(self, base_power, dmg_multiplier, mp_cost, upgraded_lv=0):
        self.__base_power = base_power
        self.__dmg_multiplier = dmg_multiplier
        self.__mp_cost = mp_cost
        self.__upgraded_lv = upgraded_lv
        self.cost_upgrade = 1000

    @property
    def base_power(self):
        return self.__base_power

    @property
    def dmg_multiplier(self):
        return self.__dmg_multiplier

    @property
    def mp_cost(self):
        return self.__mp_cost

    @property
    def upgraded_lv(self):
        return self.__upgraded_lv

    def upgrade(self):
        self.upgraded_lv += 1
        self.cost_upgrade += 1000

    def dmg(self):
        return self.base_power * self.dmg_multiplier ** self.upgraded_lv

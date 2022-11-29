class Equipment:
    def __init__(self, base_power: int, stat_multiplier: float,
                 upgraded_lv: int = 0, base: str = ''):
        self.base_power = base_power
        self.stat_multiplier = stat_multiplier
        self.upgraded_lv = upgraded_lv
        self.cost_upgrade = 1000
        self.base = base

    @property
    def base_power(self):
        return self.__base_power

    @property
    def stat_multiplier(self):
        return self.__stat_multiplier

    @property
    def upgraded_lv(self):
        return self.__upgraded_lv

    @base_power.setter
    def base_power(self, value: int):
        self.__base_power = value

    @stat_multiplier.setter
    def stat_multiplier(self, value: float):
        self.__stat_multiplier = value

    @upgraded_lv.setter
    def upgraded_lv(self, value: int):
        self.__upgraded_lv = value

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value: str):
        self.__base = value

    def upgrade(self):
        self.upgraded_lv += 1
        self.cost_upgrade += 1000

    def get_power(self):
        return self.base_power * self.stat_multiplier ** self.upgraded_lv

    def __str__(self):
        return f"Power: {self.get_power()}"

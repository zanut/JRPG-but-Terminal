class Equipment:
    def __init__(self, base_power, stat_multiplier, upgraded_lv=0):
        self.__base_power = base_power
        self.__stat_multiplier = stat_multiplier
        self.__upgraded_lv = upgraded_lv
        self.cost_upgrade = 1000

    def upgrade(self):
        self.upgraded_lv += 1
        self.cost_upgrade += 1000

    def get_power(self):
        return self.base_power * self.stat_multiplier ** self.upgraded_lv

    def __str__(self):
        return f"Power: {self.get_power()}"

    @property
    def base_power(self):
        return self.__base_power

    @property
    def stat_multiplier(self):
        return self.__stat_multiplier

    @property
    def upgraded_lv(self):
        return self.__upgraded_lv


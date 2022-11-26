class Equipment:
    def __init__(self, base_power, stat_multiplier):
        self.base_power = base_power
        self.stat_multiplier = stat_multiplier
        self.upgraded_lv = 0
        self.cost_upgrade = 1000

    def upgrade(self):
        self.upgraded_lv += 1
        self.cost_upgrade += 1000

    def get_power(self):
        return self.base_power * self.stat_multiplier ** self.upgraded_lv

    def __str__(self):
        return f"Power: {self.get_power()}"

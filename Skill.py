class Skill:
    def __init__(self, base_power, dmg_multiplier, mp_cost):
        self.base_power = base_power
        self.dmg_multiplier = dmg_multiplier
        self.mp_cost = mp_cost
        self.upgraded_lv = 0
        self.cost_upgrade = 1000

    def upgrade(self):
        self.upgraded_lv += 1
        self.cost_upgrade += 1000

    def dmg(self):
        return self.base_power * self.dmg_multiplier ** self.upgraded_lv

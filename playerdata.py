import json
from Player import Player
from Equipment import Equipment
from Skill import Skill


class PlayerData:
    def __init__(self, name=''):
        self.name = name

    def save(self, player: Player):
        new_data = {
            self.name: {
                "HP": player.hp,
                "MP": player.mp,
                "Lv": player.lv,
                "Weapon": [player.weapon.base_power,
                           player.weapon.stat_multiplier,
                           player.weapon.upgraded_lv,
                           player.weapon.base],
                "Armor": [player.armor.base_power,
                          player.armor.stat_multiplier,
                          player.armor.upgraded_lv,
                          player.armor.base],
                "Skill": [],
                "Gold": player.gold,
                "Stat": player.stat,
                "Exp": player.exp_required,
                "Point": player.point
            }
        }
        for skill in player.skill:
            new_data[self.name]["Skill"].append([skill.base_power,
                                                 skill.dmg_multiplier,
                                                 skill.mp_cost,
                                                 skill.upgraded_lv,
                                                 skill.name])

        try:
            with open("save.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError and ValueError:
            with open("save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("save.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def load(self, name):
        with open("save.json", "r") as data_file:
            data = json.load(data_file)
            player = data[name]
            return Player(lv=player["Lv"],
                          weapon=Equipment(int(player["Weapon"][0]),
                                           float(player["Weapon"][1]),
                                           int(player["Weapon"][2]),
                                           player["Weapon"][3]),
                          armor=Equipment(int(player["Armor"][0]),
                                          float(player["Armor"][1]),
                                          int(player["Armor"][2]),
                                          player["Armor"][3]),
                          skill=self.load_skill(name),
                          gold=player["Gold"],
                          name=name,
                          xp=int(player["Exp"][0]),
                          xp_need=int(player["Exp"][1]),
                          stat=player["Stat"],
                          point=int(player["Point"])
                          )

    def load_skill(self, name):
        with open("save.json", "r") as data_file:
            data = json.load(data_file)
            player = data[name]
            return [Skill(int(skill[0]),  # base_power
                          float(skill[1]),  # dmg_multiplier
                          int(skill[2]),  # mp cost
                          int(skill[3]),  # upgraded_lv
                          skill[4]  # name
                          ) for skill in player["Skill"]]

    def all_name(self):
        try:
            with open("save.json", "r") as data_file:
                data = json.load(data_file)
                return [name for name in data]
        except FileNotFoundError and ValueError:
            return []

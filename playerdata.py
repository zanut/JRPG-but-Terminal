import json
from Player import Player
from Equipment import Equipment
from Skill import Skill


class PlayerData:
    def __init__(self, name):
        self.name = name

    def save(self, Player):
        new_data = {
            self.name: {
                "HP": Player.hp,
                "MP": Player.mp,
                "Lv": Player.lv,
                "Weapon": [Player.weapon.base_power,
                           Player.weapon.dmg_multiplier,
                           Player.weapon.upgraded_lv],
                "Armor": [Player.armor.base_power,
                          Player.armor.stat_multiplier,
                          Player.armor.upgraded_lv],
                "Skill": [],
                "Gold": Player.gold,
                "Stat": Player.stat,
                "Exp": Player.exp_required,
                "Point": Player.point
            }
        }
        for i in Player.skill:
            new_data[self.name]["Skill"].append(
                [i.base_power, i.dmg_multiplier, i.mp_cost, i.upgraded_lv])

        try:
            with open("save.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError or ValueError):
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
                                           int(player["Weapon"][2])
                                           ),
                          armor=Equipment(int(player["Armor"][0]),
                                          float(player["Armor"][1]),
                                          int(player["Armor"][2])
                                          ),
                          skill=self.load_skill(name),
                          gold=player["Gold"],
                          name=name,
                          xp=int(player["Exp"][0]),
                          stat=player["Stat"],
                          point=int(player["Point"])
                          )

    def load_skill(self, name):
        with open("save.json", "r") as data_file:
            data = json.load(data_file)
            player = data[name]
            return [Skill(int(skill[0]),
                          float(skill[1]),
                          int(skill[2]),
                          int(skill[3])
                          ) for skill in player["Skill"]]

    def all_name(self):
        try:
            with open("save.json", "r") as data_file:
                data = json.load(data_file)
                return [name for name in data]
        except (FileNotFoundError or ValueError):
            print(f'None save file found')

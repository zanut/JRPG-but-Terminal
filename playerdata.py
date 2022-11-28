import json


class PlayerData:
    def __init__(self, name):
        self.name = name

    def insert(self, Player):
        new_data = {
            Player.name: {
                        "HP": Player.hp,
                        "MP": Player.mp,
                        "Lv": Player.lv,
                        "Weapon": Player.weapon.upgraded_lv,
                        "Armor": Player.armor.upgraded_lv,
                        "Skill": Player.skill.upgraded_lv,
                        "Gold": Player.gold,
                        "Stat": Player.stat,
                        "Exp": Player.exp_required,
                        "Point": Player.point
            }
        }

        try:
            with open("save.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("save.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

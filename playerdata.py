import json


class PlayerData:
    def __init__(self, name):
        self.name = name

    def insert(self, bank_account):
        new_data = {}
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

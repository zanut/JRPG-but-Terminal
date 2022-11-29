import random
import sys
import time
import csv

from Monster import Monster
from Skill import Skill


def print_withtime(sentence):
    for string in sentence:
        print(string, end='')
        sys.stdout.flush()
        time.sleep(0.01)


def print_withspace(sentence):
    print_withtime(sentence)
    print()


def generate_monster(lv):
    leval_monster = random.randint(lv - 1, lv + 1)
    rand_mons = Monster(lv=leval_monster)
    for _ in range(random.randint(1, 3)):
        skill_index = random.randint(0, len(SKILL) - 1)
        rand_mons.skill = Skill(base_power=int(SKILL[skill_index]['base_power']),
                                dmg_multiplier=float(SKILL[skill_index]['dmg_multiplier']),
                                mp_cost=int(SKILL[skill_index]['mp_cost']),
                                name=SKILL[skill_index]['name'],
                                )
    return rand_mons


SKILL = []
with open('skill_name.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        SKILL.append(r)

import random
import sys
import time
import csv

from Monster import Monster
from Skill import Skill


def print_withtime(sentence):
    """ Print each letter with 0.01 seconds delay """
    for string in sentence:
        print(string, end='')
        sys.stdout.flush()
        time.sleep(0.01)


def print_withspace(sentence):
    """ same as print_withtime but add a new line at the end """
    print_withtime(sentence)
    print()


def generate_monster(lv, skill):
    """ Generate a monster with random skill and random lv near the player lv +- 1"""
    leval_monster = random.randint(lv - 1, lv + 1)
    rand_mons = Monster(lv=leval_monster)
    for _ in range(random.randint(1, 3)):
        rand_mons.skill = generate_skill(skill)
    return rand_mons


def generate_skill(lst_obj):
    """ Generate a skill from the list of skill used for player and monster """
    skill_index = random.randint(0, len(lst_obj) - 1)
    return Skill(base_power=int(lst_obj[skill_index]['base_power']),
                 dmg_multiplier=float(lst_obj[skill_index]['dmg_multiplier']),
                 mp_cost=int(lst_obj[skill_index]['mp_cost']),
                 name=lst_obj[skill_index]['name'],
                 )


SKILL = []
with open('skill_name.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        SKILL.append(r)

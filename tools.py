import random
import sys
import time
import csv

from Monster import Monster


SKILL = []
with open('skill_name.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        SKILL.append(r)

def generate_monster(l):
    leval_monster = random.randint(l - 1, l + 1)
    rand_mons = Monster(lv=leval_monster)
    for _ in range(random.randint(1, 3)):
        rand_mons.skill = SKILL[random.randint(0, len(SKILL) - 1)]
    return rand_mons


def print_withtime(sentence):
    for string in sentence:
        print(string, end='')
        sys.stdout.flush()
        time.sleep(0.02)


def print_withspace(sentence):
    print_withtime(sentence)
    print()

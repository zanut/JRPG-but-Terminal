# Project: JRPG but Terminal

## Project overview:
#### A JRPG game style but in the terminal
JRPG game is rpg game but style of the game is turn-based and most founded in Japan. 
My project have inspired from JRPG style. However, my project convert to console style.  

## Function game
- the program have a menu to choose the character from load file.
- the program will be able to generate random monster and level of monster player character +-1 level.
- the program will be able to save the character to file.
- the program will be able to generate random skill for player every 5 level and monster will have random skill in range 1 to 3 skills.
- the program will be able to upgrade the character's skill, armor, weapon.
- the program will be able to upgrade status of the character.



## detail of all class implemented in this project:
-  #### Monster  from Monster.py
This class will generate object of monster. also, this class will generate monster detail such as, hp, mp and how monster action
-  #### Player  from Player.py
This class will generate object of player. generate player detail similar to monster detail such as, hp, mp. However, this class also have Equipment class and Skill class and have different way to calculate player hp, mp, dmg
-  #### Mechanical from Mechanical.py
This class control all game mechanic such as, fight, upgrade, save, load, etc
-  #### Equipment from Equipment.py
This class generate weapon and armor for player. also, have feature to upgrade equipment
-  #### Skill  from Skill.py
This class function almost same as Equipment class. However, this class both player and monster can use skill
-  #### PlayerData  from PlayerData.py
This class manage to save or load player data such as, name, gold, lv, exp, Skill class, Equipment class, etc

### In additional file:  
-  #### tools.py
this file store all useful function that use in other class
-  #### skill_name.csv  
this file store all monster skill also, have room to improved
-  #### Ascii_model.py  
this file store all ascii model and have room to improved same as skill_name.csv
-  #### main.py  
this file combine all class together and run the game

## Future improvement:
- add more ascii model
- add more skill
- add type of monster such as boss, mini boss, etc
- add more feature such as, shop, etc

## How to run the game:

crete folder name : xxxxx (whatever you want)  

Terminal command
```
git clone https://github.com/zanut/JRPG-but-Terminal.git xxxxx(replace folder name)  

cd filelocation (something like this C:\Users\user\Documents\xxxxxx)

python3 main.py
```
if it doesn't work, try this command
```
python main.py
```
### Requirement
- #### python 3.8 or above


## How to play the game:
1. Crete new character or load character from menu
2. Choose the action if you want to fight enter 'y' in the terminal
3. If you want to save/load the game, choose save/load from base
4. If you want to upgrade the character, choose upgrade from base
5. If you want to exit the game, choose exit from base

GitHub profile:
```
https://github.com/zanut/JRPG-but-Terminal.git
```

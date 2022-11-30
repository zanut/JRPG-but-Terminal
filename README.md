# Project: JRPG but Terminal

## Project overview:
##### A JRPG game style but in the terminal
JRPG game is rpg game but style of the game is turnbased and most founded in Japan. 
My project have inspired from JRPG style. However, my project convert to console style.  

detail of all class implemented in this project:
-  ##### Monster  from Monster.py
This class will generate object of monster. also, this class will generate monster detail such as, hp, mp and how monster action
-  ##### Player  from Player.py
This class will generate object of player. generate player detail similar to monster detail such as, hp, mp. However, this class also have Equipment class and Skill class and have different way to calculate player hp, mp, dmg
-  ##### Mechanical from Mechanical.py
This class control all game mechanic such as, fight, upgrade, save, load, etc
-  ##### Equipment from Equipment.py
This class generate weapon and armor for player. also, have feature to upgrade equipment
-  ##### Skill  from Skill.py
This class function almost same as Equipment class. However, this class both player and monster can use skill
-  ##### PlayerData  from PlayerData.py
This class manage to save or load player data such as, name, gold, lv, exp, Skill class, Equipment class, etc

### In additional file:  
- skill_name.csv  
this file store all monster skill also, have room to improved
- Ascii_model.py  
this file store all ascii model and have room to improved same as skill_name.csv
- main.py  
this file combine all class together and run the game

## How to run the game:
1.  Clone the project or download the project from GITHUB exclude file name : .idea , pycache and save.json if you want to start new game
2.  Open terminal and go to the project directory by cd location of the project
3.  Run the game by type python3 main.py or python main.py

https://github.com/zanut/JRPG-but-Terminal

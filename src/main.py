import random
import resources
from resources import player, teammate, enemy
import names
import os
import time
enemygennumber = 0
classes = ["Warrior", "Paladin", "Hunter" , "Rouge" , "Priest" , "Shaman" , "Mage" , "Warlock" , "Monk" , "Druid" , "Demon Hunter" , "Death Knight" ]
races = ["Human", "Dwarf", "Night Elf", "Gnome", "Draenei", "Worgen", "Pandaren", "Void Elf", "Lightforged Draenei", "Dark Iron Dwarf", "Kul Tiran", "mechagnome"]
teammates = []
enemies = []
user = 0
round = 1

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def loader():
    loading = 0
    while True:    
        loading +=random.randint(1,10)
        print(f"Loading, {loading}% Done")
        if loading > 90:
            loading = 100
            print(f"Loading, {loading}% Done")
            clearConsole()
            print("Loading Complete!")
            break
        time.sleep(0.05)

def charactercreator():    
    while True:
        classchoice = input("> Select class. Type Help for list of all classes: ")
        if classchoice.title() in classes:
            classchoice = classchoice.title()
            break
        elif classchoice.capitalize() == "Help":
            print("\nClasses avalabile are :",end = ' ')
            print(*classes, sep =", ")
        else:
            print("Try again")
    while True:
        racechoice = input("> Select race. Type Help for list of all races: ")
        if racechoice.title() in races:
            racechoice = racechoice.title()
            break
        elif racechoice.capitalize() == "Help":
            print("\nRaces avalabile are :",end = ' ')
            print(*races, sep =", ")
        else:
            print("Try again")
    user = resources.player(random.randint(10000,30000),random.randint(2500,7500),classchoice,random.randint(1,50),names.get_first_name(), racechoice)

    print(f"Health: {user.health}\nAttack: {user.attackpower}\nClass: {user.spec}\nArmor: {user.armor}\nName: {user.name}\nRace: {user.race}")

def main():
    loader()
    while True:
        global teamgennumber
        choice = input("""
> WoW Arena Simulator 2022

> 1. 2v2
> 2. 3v3
> 3. Battlegrounds
> 4. Custom Match

> © AP Industries 2022, All rights reserved.

> Input[1,2,3,4] """)
        if choice == "1":
            teamgennumber = 1
            enemygennumber = 2
            break
        elif choice == "2":
            teamgennumber = 2
            enemygennumber = 3
            break
        elif choice == "3": 
            teamgennumber = 19
            enemygennumber = 20
            break
        elif choice == "4":
            custommatchchoice = int(input("> How many characters do you want on each team?:  "))
            enemygennumber = custommatchchoice
            teamgennumber = custommatchchoice-1
            
            break
        else:
            print("Try again")
    print(teamgennumber)
    
    charactercreator()

    teammategenerator()

def teammategenerator():
    print(teamgennumber)
    teammatenumber = 0
    for i in range(teamgennumber):
        teammate = resources.player(random.randint(10000,30000),random.randint(2500,7500),random.choice(classes),random.randint(1,50),names.get_first_name(), random.choice(races))
        globals()[f"teammate{i}"] = teammate
        print(f"Health: {teammate.health}\nAttack: {teammate.attackpower}\nClass: {teammate.spec}\nArmor: {teammate.armor}\nName: {teammate.name}\nRace: {teammate.race}")
        teammates.append(teammate)
    



main()
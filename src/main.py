import random
import resources
from resources import player, teammate, enemy
import names
import os
import time
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
        global enemygennumber
        choice = input("""
> WoW Simulator 2022

> 1. 2v2
> 2. 3v3
> 3. Battlegrounds
> 4. Custom Match
> 5. Raiding
> 6. Dungeons

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
    print(f"Team generator number{teamgennumber}")
    print(f"Enemy generator number{enemygennumber}")
    charactercreator()

    teammategenerator()

    enemygenerator()

def teammategenerator():
    print(f"Team generator number{teamgennumber}")
    for i in range(teamgennumber):
        teammatecurrent = resources.teammate(random.randint(10000,30000),random.randint(2500,7500),random.choice(classes),random.randint(1,50),names.get_first_name(), random.choice(races))
        print(f"Health: {teammatecurrent.health}\nAttack: {teammatecurrent.attackpower}\nClass: {teammatecurrent.spec}\nArmor: {teammatecurrent.armor}\nName: {teammatecurrent.name}\nRace: {teammatecurrent.race}\n")
        globals()['teammate%s' % i] = teammatecurrent
        teammates.append(teammatecurrent)
    hey = 0
    for i in teammates:
        hey += 1
        print(hey)

def enemygenerator():
    print(f"Enemy generator number{enemygennumber}")
    for i in range(enemygennumber):
        enemycurrent = resources.enemy(random.randint(10000,30000),random.randint(2500,7500),random.choice(classes),random.randint(1,50),names.get_first_name(), random.choice(races))
        print(f"Health: {enemycurrent.health}\nAttack: {enemycurrent.attackpower}\nClass: {enemycurrent.spec}\nArmor: {enemycurrent.armor}\nName: {enemycurrent.name}\nRace: {enemycurrent.race}\n")
        globals()['teammate%s' % i] = enemycurrent
        enemies.append(enemycurrent)
    heye = 0
    for i in enemies:
        heye += 1
        print(heye)




main()
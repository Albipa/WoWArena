import random
import Resources

teamgennumber = 0
enemygennumber = 0
classes = ["Warrior", "Paladin", "Hunter" , "Rouge" , "Priest" , "Shaman" , "Mage" , "Warlock" , "Monk" , "Druid" , "Demon hunter" , "Death knight" ]
teammates = []
enemies = []

class player:
    def __init__(self, health, attackpower, spec, armor):
        self.health = health
        self.attackpower = attackpower
        self.spec = spec
        self.armor = armor

def main():
    while True:
        choice = input("""
> WoW Arena Simulator 2022

> 1. 2v2
> 2. 3v3
> 3. Battlegrounds

> © AP Industries 2022, All rights reserved.

> Input[1,2,3] > """)
        print(choice)
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
        else:
            print("Try again")
    teamgenerator()
    enemygenerator()
    print(teamgennumber)
    print(enemygennumber)
    print(teammates)
    print(enemies)
    for i in range(teamgennumber):
        classchoice = random.choice(classes)
        healthchoice = random.randint(10000,50000)
        attackpowerchoice = random.randint(2500,7500) 
        teammates.append(player(healthchoice,attackpowerchoice,classchoice))
        print("Hey")
    

def teamgenerator():
    for i in range(teamgennumber):
        classchoice = random.choices(classes)
        healthchoice = random.randint(10000,50000)
        attackpowerchoice = random.randint(2500,7500) 
        teammates.append(player(healthchoice,attackpowerchoice,classchoice))
        print("Hey")

def enemygenerator():
    for i in range(enemygennumber):
        classchoice = random.choices(classes)
        healthchoice = random.randint(10000,50000)
        attackpowerchoice = random.randint(2500,7500) 
        enemies.append(player(healthchoice,attackpowerchoice,classchoice))
        print("Heel")



main()
class player:
    def __init__(self, health, attackpower, spec, armor, name, race):
        self.health = health
        self.attackpower = attackpower
        self.spec = spec
        self.armor = armor
        self.name = name
        self.race = race

    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_attackpower(self):
        return self.attackpower

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name

class teammate:
    def __init__(self, health, attackpower, spec, armor, name, race):
        self.health = health
        self.attackpower = attackpower
        self.spec = spec
        self.armor = armor
        self.name = name
        self.race = race
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_attackpower(self): # tidigare damage
        return self.attackpower

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name

class enemy:
    def __init__(self, health, attackpower, spec, armor, name, race):
        self.health = health
        self.attackpower = attackpower
        self.spec = spec
        self.armor = armor
        self.name = name
        self.race = race

    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_attackpower(self): # tidigare damage
        return self.attackpower

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name

'''A class to represent an enemy in an RPG.'''

class Enemy:
    '''An enemy in an RPG.'''
    def __init__(self):
        self.name = "enemy"
        self.level = 1
        self.attack = 10 # damage on hit
        self.defense = 10 # damage reduction when hit
        self.health = 10

    def __str__(self):
        return f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"

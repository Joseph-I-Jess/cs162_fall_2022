'''Represent an item in an RPG.'''

class Item:
    def __init__(self, name="an item", attack=0, defense=0, health=0):
        self.name = name
        self.attack = attack # damage on hit
        self.defense = defense # damage reduction when hit
        self.health = health
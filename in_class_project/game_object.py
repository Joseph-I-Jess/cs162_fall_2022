'''Represent an abstract object in this game.'''

class Game_object:
    EQUIPMENT_SLOTS = ["weapon", "armor", "accessory"]
    
    def __init__(self, graphical_id=None, graphics_file=None, location=None, name="an item", attack=0, defense=0, health=0):
        self.graphical_id = graphical_id # to be used if this object is drawn on a graphical space
        self.graphics_file = graphics_file # path to gaphics file for this object if it exists
        self.location = location
        self.name = name
        self.attack = attack # damage on hit
        self.defense = defense # damage reduction when hit
        self.health = health
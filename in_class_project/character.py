'''Create and manage a character'''

class Character:
    '''Player character class.'''
    def __init__(self):
        self.graphical_id = None # to be used if this object is drawn on a graphical space
        self.location = None
        self.name = "hero"
        self.level = 1
        self.attack = 10 # damage on hit
        self.defense = 10 # damage reduction when hit
        self.health = 10

    def set_location(self, new_location=None):
        self.location = new_location

    def __str__(self):
        return f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"
'''Create and manage a character'''

class Character:
    '''Player character class.'''
    def __init__(self):
        self.name = "hero"
        self.level = 1
        self.attack = 10 # damage on hit
        self.defense = 10 # damage reduction when hit
        self.health = 10

    def __str__(self):
        return f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"
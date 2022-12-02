'''Abstract class to represent characters and enemies in this game.'''

class Being:
    '''A being, which is either a character or an enemy.'''

    DEFAULT_ATTACK = 10
    DEFAULT_DEFENSE = 10
    DEFAULT_HEALTH = 10

    def __init__(self, graphical_id=None, location=None, name="being", level=1, attack=DEFAULT_ATTACK, defense=DEFAULT_DEFENSE, health=DEFAULT_HEALTH, inventory={}, equipment={}):
        self.graphical_id = graphical_id # to be used if this object is drawn on a graphical space
        self.location = location
        self.name = name
        self.level = level
        
        self.attack = attack # damage on hit
        self.defense = defense # damage reduction when hit
        self.health = health
        
        self.inventory = inventory # all items the character carries
        self.equipment = equipment # items that are equipped on the character

    def __str__(self):
        result = f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"
        result += f"\nitems:"
        for item in self.inventory:
            result += "\n\t"
            if item in self.equipment:
                result += "(equipped) "
            result += f"{self.inventory[item].name}"

        return result

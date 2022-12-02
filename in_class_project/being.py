'''Abstract class to represent characters and enemies in this game.'''

import in_class_project.game_object as game_object

class Being(game_object.Game_object):
    '''A being, which is either a character or an enemy.'''

    DEFAULT_ATTACK = 10
    DEFAULT_DEFENSE = 10
    DEFAULT_HEALTH = 10

    def __init__(self, graphical_id=None, graphics_file=None, location=None, name="being", level=1, attack=DEFAULT_ATTACK, defense=DEFAULT_DEFENSE, health=DEFAULT_HEALTH, inventory={}, equipment={}):
        super().__init__(graphical_id, graphics_file, location, name, attack, defense, health)
        self.level = level
        
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

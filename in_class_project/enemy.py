'''A class to represent an enemy in an RPG.'''

import in_class_project.being as being

class Enemy(being.Being):
    '''An enemy in an RPG.'''
    def __init__(self, graphical_id=None, graphics_file=None, location=None, name="enemy", level=1, attack=being.Being.DEFAULT_ATTACK, defense=being.Being.DEFAULT_DEFENSE, health=being.Being.DEFAULT_HEALTH, inventory: list=None, equipment: dict=None):
        super().__init__(graphical_id, graphics_file, location, name, level, attack, defense, health, inventory, equipment)

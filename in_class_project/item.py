'''Represent an item in an RPG.'''

import in_class_project.game_object as game_object

"""
    ToDo:
        Add type to Item for equipment, consumable, or quest
"""

class Item(game_object.Game_object):

    DEFAULT_ATTACK = 0
    DEFAULT_DEFENSE = 0
    DEFAULT_HEALTH = 0

    def __init__(self, graphical_id=None, location=None, name="an item", attack=DEFAULT_ATTACK, defense=DEFAULT_DEFENSE, health=DEFAULT_HEALTH, type="equipment"):
        super().__init__(graphical_id, location, name, attack, defense, health)

        self.type = type
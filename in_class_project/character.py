'''Create and manage a character'''

import in_class_project.being as being

"""
    ToDo:
        should stats be a dictionary of stats for easier modification by items, powers, etc. later?
        Should some stats (or all stats) have a current stat and a maximum stat?
"""

class Character(being.Being):
    '''Player character class.'''

    DEFAULT_CHARACTER_GRAPHICS_FILE_PATH = ".\in_class_project\images\player.png"

    # add type hints!?
    def __init__(self, graphical_id=None, graphics_file=DEFAULT_CHARACTER_GRAPHICS_FILE_PATH, location=None, name="hero", level=1, attack=being.Being.DEFAULT_ATTACK, defense=being.Being.DEFAULT_DEFENSE, health=being.Being.DEFAULT_HEALTH, inventory: list=None, equipment: dict=None):
        super().__init__(graphical_id, graphics_file, location, name, level, attack, defense, health, inventory, equipment)

    def set_location(self, new_location=None):
        self.location = new_location

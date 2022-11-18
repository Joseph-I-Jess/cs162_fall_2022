'''Manage RPG data model.'''

import in_class_project.character as character

class Rpg:
    '''Main rpg management class.'''

    def __init__(self):
        self.player = character.Character()

    def get_player_string(self):
        return self.player.__str__()

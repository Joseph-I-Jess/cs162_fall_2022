'''Manage RPG data model.'''

import random

import in_class_project.character as character
import in_class_project.command_interpreter as command_interpreter
import in_class_project.enemy as enemy
import in_class_project.map_cell as map_cell

"""
    ToDo:
        make fight more fun, do not allow defeated beings from participating!
"""

class Rpg:
    '''Main rpg management class.'''

    def __init__(self):
        self.player = character.Character()
        self.player_location = None
        self.enemy = enemy.Enemy()
        self.map_cells = []
        
        # initialize map...
        first_map_cell = map_cell.Map_cell("starting room", "Just the starting room of our game...", [self.enemy], [], 0, 0, {})
        self.map_cells.append(first_map_cell)

        second_map_cell = map_cell.Map_cell("room to the north", "North of the starting room of our game...", [], [], 0, 1, {})
        first_map_cell.add_exit("north", second_map_cell)
        self.map_cells.append(second_map_cell)

        # set players starting position
        self.player_location = first_map_cell

        # initialize the command interpreter
        self.command_interpreter = command_interpreter.Command_interpreter(self)
        self.command_interpreter.set_fight_command(self.fight)
        self.command_interpreter.set_move_command(self.move)

    def interpret_command(self, proposed_command):
        '''Pass command to interpreter and return result to caller.'''
        return self.command_interpreter.interpret_command(proposed_command)

    def get_player_string(self):
        return self.player.__str__()

    def fight(self, proposed_enemy_name: str) -> str:
        '''Either fight the proposed enemy or return that the enemy does not exist (without other side effects)'''

        # result of this function...
        result = ""

        # check that this enemy exists
        proposed_enemy = None
        for enemy in self.player_location.enemies:
            if enemy.name == proposed_enemy_name:
                proposed_enemy = enemy

        if proposed_enemy is None:
            result = "There is no enemy with that name in your current room."
        else:
            player_result = ""
            enemy_result = ""
            # single round of combat
            # player attacks enemy
            damage_to_enemy = (self.player.attack + random.randrange(0, 3)) - proposed_enemy.defense
            proposed_enemy.health -= damage_to_enemy

            if proposed_enemy.health <= 0:
                proposed_enemy.health = 0
                enemy_result = f"\nThe {proposed_enemy.name} is defeated!"
                self.player_location.enemies.remove(proposed_enemy)
            
            enemy_result = f"damage done to enemy: {damage_to_enemy}, leaving it with {proposed_enemy.health} health left." + enemy_result

            # enemy attacks player
            damage_to_player = (proposed_enemy.attack + random.randrange(0, 3)) - self.player.defense
            self.player.health -= damage_to_player

            if self.player.health <= 0:
                self.player.health = 0
                player_result = f"\nThe {self.player.name} is defeated!"
            
            player_result = f"damage done to player: {damage_to_player}, leaving it with {self.player.health} health left." + player_result

            result = enemy_result + "\n" + player_result

        return result

    def move(self, proposed_exit_string: str) -> str:
        '''Attempt to move player from current map_cell through exit to destination map_cell and return a string either of the new map_cell or an invalid message.'''
        result = ""
        # need to check if that proposed_exit_string is a valid exit from the current room
        current_location_exits = self.player_location.exits
        if proposed_exit_string in current_location_exits:
            # if valid, move player to new room
            self.player_location = current_location_exits[proposed_exit_string]
            result = f"You have entered \"{self.player_location.name}\""
        else:
            # possible return of invalid value
            result = f"{proposed_exit_string} is an invalid exit"
        
        return result

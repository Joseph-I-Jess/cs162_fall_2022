'''Manage RPG data model.'''

import random

import in_class_project.character as character
import in_class_project.command_interpreter as command_interpreter
import in_class_project.enemy as enemy
import in_class_project.item as item
import in_class_project.map_cell as map_cell

"""
    ToDo:
        make fight more fun, do not allow defeated beings from participating!
        make look also work with specified enemy or item!
        make map cells show up on rpg window GUI!
        make items and update places that should involve them!
"""

class Rpg:
    '''Main rpg management class.'''

    def __init__(self):
        self.player = character.Character()

        self.enemy = enemy.Enemy()
        self.map_cells = []
        
        # initialize map...
        first_map_cell = map_cell.Map_cell(name="starting room", description="Just the starting room of our game...", beings=[self.player, self.enemy], items={}, x=0, y=0, exits={})
        self.map_cells.append(first_map_cell)

        dagger = item.Item("dagger", attack=3, defense=1)
        second_map_cell = map_cell.Map_cell("room to the south", "North of the starting room of our game...", [], {dagger.name: dagger}, 0, 1, {"north":first_map_cell})
        first_map_cell.add_exit("south", second_map_cell)
        self.map_cells.append(second_map_cell)

        # set players starting position
        self.player.set_location(first_map_cell)

        # initialize the command interpreter
        self.command_interpreter = command_interpreter.Command_interpreter(self)
        self.command_interpreter.set_command("fight", self.fight, "fight <enemy>", ["fight", "f"])
        self.command_interpreter.set_command("move", self.move, "move <direction>", ["move", "m"])
        # instead of exit we could do a save and quit method!
        self.command_interpreter.set_command("exit", exit, "exit", ["exit", "quit", "q", "ragequit"])
        self.command_interpreter.set_command("stats", lambda my_list: self.player.__str__(), "stats", ["stats", "s"])
        self.command_interpreter.set_command("look", self.look, "look", ["look", "l"])
        self.command_interpreter.set_command("get", self.get, "get <item>", ["get", "g"])
        self.command_interpreter.set_command("equip", self.player.equip, "equip <equipment name>", ["equip", "e"])
        self.command_interpreter.set_command("unequip", self.player.unequip, "unequip <equipment name>", ["unequip", "u"])

        self.view = None

    def set_view(self, proposed_view):
        self.view = proposed_view

    def update_view(self):
        if self.view is not None:
            self.view.set_map_data(self.map_cells)

    def get_map_data(self) -> list[map_cell.Map_cell]:
        return self.map_cells

    def interpret_command(self, proposed_command):
        '''Pass command to interpreter and return result to caller.'''
        return self.command_interpreter.interpret_command(proposed_command)

    def get_player_string(self):
        return self.player.__str__()

    def fight(self, proposed_enemy_names: list[str]) -> str:
        '''Either fight the first proposed enemy or return that the enemy does not exist (without other side effects)'''

        # result of this function...
        result = ""

        # check that this enemy exists
        proposed_enemy = None
        for enemy in self.player.location.beings:
            if enemy.name == proposed_enemy_names[1]:
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
                self.player.location.beings.remove(proposed_enemy)
                # update view
                self.update_view()
            
            enemy_result = f"damage done to enemy: {damage_to_enemy}, leaving it with {proposed_enemy.health} health left." + enemy_result

            # enemy attacks player
            damage_to_player = (proposed_enemy.attack + random.randrange(0, 3)) - self.player.defense
            self.player.health -= damage_to_player

            if self.player.health <= 0:
                self.player.health = 0
                player_result = f"\nThe {self.player.name} is defeated!"
                # should we remove the player from the location and update the view?
            
            player_result = f"damage done to player: {damage_to_player}, leaving it with {self.player.health} health left." + player_result

            result = enemy_result + "\n" + player_result

        return result

    def move(self, proposed_exit_strings: list[str]) -> str:
        '''Attempt to move player from current map_cell through exit to destination map_cell and return a string either of the new map_cell or an invalid message.'''
        result = ""
        # need to check if that proposed_exit_string is a valid exit from the current room
        current_location_exits = self.player.location.exits
        if len(proposed_exit_strings) >= 2 and proposed_exit_strings[1] in current_location_exits:
            # if valid, move player to new room
            new_room = current_location_exits[proposed_exit_strings[1]]
            # remove player from current map_cell list
            self.player.location.beings.remove(self.player)
            # change player's internal location
            self.player.set_location(new_room)
            # add player to new map_cell list
            new_room.beings.append(self.player)
            # update view
            self.update_view()
            # prompt that change succeeded
            result = f"You have entered \"{self.player.location.name}\""
        else:
            # possible return of invalid value
            result = f"{proposed_exit_strings} is an invalid exit"
        
        return result

    def look(self, proposed_objects: list[str]=None) -> str:
        '''Look at some propopsed object or the room by default.'''
        
        result = ""
        
        if len(proposed_objects) <= 1:
            # room look
            current_room = self.player.location

            result += f"{current_room.name}\n"
            result += f"\t{current_room.description}\n"
            result += "exits:\n"
            if len(current_room.exits) <= 0:
                result += "\tNo obvious exits!"
            else:
                for exit_direction in current_room.exits.keys():
                    result += f"\t{exit_direction}\n"

            # enemies in room
            if len(current_room.beings) >= 1:
                result += "beings:\n"
                for enemy in current_room.beings:
                    result += f"\t{enemy.name}\n"

            # items in room
            if len(current_room.items) >= 1:
                result += "items:\n"
                for item in current_room.items:
                    result += f"\t{current_room.items[item].name}\n"

            return result

    def get(self, proposed_item_names: list[str]) -> str:
        result = ""
        
        if len(proposed_item_names) >= 2 and proposed_item_names[1] in self.player.location.items:
            proposed_item_name = proposed_item_names[1]
            proposed_item = self.player.location.items[proposed_item_name]

            # remove item from room
            self.player.location.items.pop(proposed_item_name, None)

            # add item to player inventory
            self.player.inventory[proposed_item_name] = proposed_item

            result = f"got {proposed_item_name}!"
        else:
            result = f"No item named {proposed_item_name} in this room"

        return result


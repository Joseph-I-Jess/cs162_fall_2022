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
        self.player = character.Character() # use default character graphics file path

        dagger1 = item.Item(name="dagger1", attack=4, defense=1, slot="weapon")
        dagger2 = item.Item(name="dagger2", attack=5, slot="weapon")
        leather_shirt = item.Item(name="leather_shirt", defense=2, slot="armor")

        # self.enemy = enemy.Enemy(inventory=[dagger1, dagger2, leather_shirt])
        # # equip an item on an enemy
        # self.enemy.equip(["equip", "leather_shirt"])
        # alternatively create the enemy with the correct attributes
        self.enemy = enemy.Enemy(inventory=[dagger1, dagger2, leather_shirt], equipment={"leather_shirt":leather_shirt})
        self.enemy.equipment_slots["armor"] = leather_shirt
        self.map_cells = []
        
        # initialize map...
        first_map_cell = map_cell.Map_cell(name="starting room", description="Just the starting room of our game...", beings=[self.player, self.enemy], x=0, y=0)
        self.map_cells.append(first_map_cell)

        dagger = item.Item(name="dagger", attack=3, defense=1, slot="weapon")
        second_map_cell = map_cell.Map_cell(name="room to the south", description="south of the starting room of our game...", items=[dagger], x=0, y=1)
        first_map_cell.add_exit("south", second_map_cell)
        second_map_cell.add_exit("north", first_map_cell)
        self.map_cells.append(second_map_cell)

        map_cell_1_0 = map_cell.Map_cell(name="east of starting room", description="east of the starting room of our game...", x=1, y=0)
        first_map_cell.add_exit("east", map_cell_1_0)
        self.map_cells.append(map_cell_1_0)

        map_cell_1_1 = map_cell.Map_cell(name="east of second map cell", description="east of the second room of our game...", x=1, y=1)
        second_map_cell.add_exit("east", map_cell_1_1)
        self.map_cells.append(map_cell_1_1)

        map_cell_3_4 = map_cell.Map_cell(name="out in the open", description="south-east of the rest of the map", x=3, y=4)
        map_cell_1_0.add_exit("up-elevator", map_cell_3_4)
        map_cell_1_1.add_exit("up-elevator", map_cell_3_4)
        map_cell_3_4.add_exit("drop-down", first_map_cell)
        self.map_cells.append(map_cell_3_4)

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

        self.command_interpreter.set_command("save", self.save, "save", ["save"])

        # We could even have commands based on functions rather than methods!
        self.command_interpreter.set_command("recurse", recurse, "recurse", ["recurse"])

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
                self.player.location.items.extend(proposed_enemy.inventory)
                # alternatively:
                # for current_item in proposed_enemy.inventory:
                #     self.player.location.items.append(current_item)
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
                result += "\tNo obvious exits!\n"
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
                    result += f"\t{item.name}\n"

        else:
            # look at specific object with name
            # if we get here we have 2 or more strings in the input list
            # order of target of look: beings, items, then exits
            current_location = self.player.location
            proposed_object_name = proposed_objects[1]
            category_spacer = "\n" + 30*"-" + "\n"
            
            # beings
            if any(proposed_object_name == being.name for being in current_location.beings):
                result += f"beings named {proposed_object_name}:"
                result += category_spacer
                for being in current_location.beings:
                    if proposed_object_name == being.name:
                        result += f"{being.__str__()}"
                result += category_spacer
            else:
                result += f"No beings named {proposed_object_name}\n\n"
            
            #items in room
            if any(proposed_object_name == item.name for item in current_location.items):
                result += f"items named {proposed_object_name}:"
                result += category_spacer
                for item in current_location.items:
                    if proposed_object_name == item.name:
                        result += f"{item.__str__()}"
                result += category_spacer
            else:
                result += f"No items named {proposed_object_name}\n\n"
            
            #items in player inventory
            if any(proposed_object_name == item.name for item in self.player.inventory):
                result += f"inventory items named {proposed_object_name}:"
                result += category_spacer
                for item in self.player.inventory:
                    if proposed_object_name == item.name:
                        result += f"{item.__str__()}"
                result += category_spacer
            else:
                result += f"No inventroy items named {proposed_object_name}\n\n"

            #exits in room
            if proposed_object_name in current_location.exits:
                result += f"Exit {proposed_object_name} leads to:\n"
                result += category_spacer
                result += f"{current_location.exits[proposed_object_name].__str__()}"
                result += category_spacer
            else:
                result += f"No exits named {proposed_object_name}\n\n"

        return result

    def get(self, proposed_item_names: list[str]) -> str:
        result = ""
        
        if len(proposed_item_names) >= 2:
            proposed_item_name = proposed_item_names[1]
        
        proposed_item = None
        # find first instance of item with thae proposed name
        for current_item in self.player.location.items:
            if current_item.name == proposed_item_name:
                proposed_item = current_item
                break

        if proposed_item is not None:
            # remove item from room
            self.player.location.items.remove(proposed_item)

            # add item to player inventory
            # fix this to be a list instead of a dictionary...
            self.player.inventory.append(proposed_item)

            result = f"got {proposed_item_name}!"
        else:
            result = f"No item named {proposed_item_name} in this room"

        self.update_view()

        return result

    def save(self, args):
        '''Save player data to a file.'''
        result = "Save failed!"

        with open(f"{self.player.name}.sav", "w") as output_file:
            output_file.write(self.player.__str__())
            result = f"Save for {self.player.name} succeeded!"

        return result

def recurse(str_list: list[str]) -> str:
    '''Check and fetch first value, make sure it is an int.'''
    result = "invalid use of recurse... go look it up..."

    if len(str_list) >= 2 and str_list[1].isnumeric():
        result = f" the factorial of {str_list} is: {recurse_helper(int(str_list[1]))}!"

    return result

def recurse_helper(end: int) -> int:
    '''Show recursion with this factorial function...'''
    if end in [0, 1]:
        return 1
    elif end < 0:
        return -1
    
    return end * recurse_helper(end - 1)

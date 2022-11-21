"""Represent a single map cell in an RPG."""

class Map_cell:
    def __init__(self, name: str="no name given", description: str="no description given", enemies: list=[], items:list=[], x: int=0, y: int=0, exits: list=[]):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.items = items
        self.x = x
        self.y = y
        self.exits = exits

    def add_exit(self, proposed_name: str, proposed_map_cell):
        """Add new exit to this map cell with proposed_name mapping to proposed_map_cell if not already in use, otherwise return an error message."""
        if proposed_name in self.exits.keys():
            return "That exit name ({proposed_name}) is already in use in this room ({self.name})"
        else:
            # should we check anything about the proposed map cell...?
            self.exits[proposed_name] = proposed_map_cell

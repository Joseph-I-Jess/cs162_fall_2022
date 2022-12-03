'''Represent a single map cell in an RPG.'''

"""
    ToDo:
        make add and remove item methods?
        make add and remove being methods?
"""

class Map_cell:
    def __init__(self, name: str="no name given", description: str="no description given", beings: list=None, items:list=None, x: int=0, y: int=0, exits: dict=None):
        self.graphical_id = None # to be used if this object is drawn on a graphical space
        self.name = name
        self.description = description
        self.beings = beings if beings is not None else list()
        self.items = items if items is not None else list()
        self.x = x
        self.y = y
        self.exits = exits if exits is not None else dict()

    def add_exit(self, proposed_name: str, proposed_map_cell):
        """Add new exit to this map cell with proposed_name mapping to proposed_map_cell if not already in use, otherwise return an error message."""
        if proposed_name in self.exits.keys():
            return "That exit name ({proposed_name}) is already in use in this room ({self.name})"
        else:
            # should we check anything about the proposed map cell...?
            self.exits[proposed_name] = proposed_map_cell

    def __str__(self):
        result = f"name: {self.name}\ndescription: {self.description}\n"
        
        result += "beings:\n"
        for being in self.beings:
            result += f"\t{being.name}\n"

        result += "items:\n"
        for item in self.items:
            result += f"\t{item.name}\n"

        result += "exits:\n"
        for exit in self.exits:
            result += f"\t{exit}\n"

        return result

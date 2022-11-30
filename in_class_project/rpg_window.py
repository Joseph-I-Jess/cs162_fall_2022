import tkinter as tk

import in_class_project.character as character
import in_class_project.enemy as enemy

"""
    ToDo:
        .Add move capability to input handler
        .Move get_input to its own command interpreter class...
        Add map_cells to the Map part of the Rpg_window
        Add Item class, add item behavior to character, enemy, and map_cell
"""

class Rpg_window:
    '''The main window of this RPG project.
    
        Graphical components are meant to have data insertted for display.
    '''
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x750")
        
        # init map
        self.map = tk.Canvas(self.root, width=512, height=375, background="dark gray")
        self.map.grid(column=0, row=0, columnspan=6)

        self.map_cell_size = 40
        self.map_cell_gap = 10
        self.map_cell_color = "white"
        self.map_player_color = "green" # top left
        self.map_enemy_color = "red" # top right
        self.map_item_color = "yellow" # bottom left
        self.map_cell_exit_color = "brown" # bottom right

        # init character
        self.character = tk.Text(self.root, width=63, height=23)
        self.character.grid(column=6, row=0, columnspan=6)

        # init output
        self.output = tk.Text(self.root, width=63, height=18)
        self.output.grid(column=0, row=1, columnspan=6)

        # init input
        self.input = tk.Entry(self.root, width=60)
        self.input.grid(column=0, row=2, columnspan=5)
        self.input.bind('<Return>', lambda event: self.get_input())
        self.submit = tk.Button(self.root, text="submit", command=self.get_input)
        self.submit.grid(column=5, row=2, columnspan=1)

        self.input.focus_set()

        self.model = None

    def insert_into_character(self, character_string: str):
        self.character.insert(tk.INSERT, character_string)

    def get_input(self):
        '''Get input from input box and pass it to the command interpreter.'''
        input_string = self.input.get()

        if self.model is not None:
            result = self.model.interpret_command(input_string)
        else:
            print("The model has not been set in this window!")
            raise ModelNotInitiializedError()

        self.output.insert(tk.END, f"{result}\n")
        self.output.yview(tk.END)

    def set_model(self, proposed_model):
        self.model = proposed_model

    def set_map_data(self, new_map_data=None) -> None:
        '''Clear and redraw map, or just clear it if new map data is none.'''
        for current_map_cell in new_map_data:
            # fetch x, y, coordinates to draw room
            # where should my gap be?  Fix to have gaps included!
            # should we change this to be a line between rooms that connect?
            current_map_cell_x0 = (current_map_cell.x * self.map_cell_size) + self.map_cell_gap
            current_map_cell_y0 = (current_map_cell.y * self.map_cell_size) + self.map_cell_gap
            current_map_cell_x1 = (current_map_cell.x * self.map_cell_size) + self.map_cell_size + self.map_cell_gap
            current_map_cell_y1 = (current_map_cell.y * self.map_cell_size) + self.map_cell_size + self.map_cell_gap
            current_map_cell.graphical_id = self.map.create_rectangle(current_map_cell_x0, current_map_cell_y0, current_map_cell_x1, current_map_cell_y1, fill=self.map_cell_color)

            # draw beings with a color based on whether it is a player or an enemy
            for being in current_map_cell.beings:
                # player has no x offset or y offset
                being_x0 = current_map_cell_x0
                being_y0 = current_map_cell_y0
                being_x1 = current_map_cell_x0 + self.map_cell_size / 2
                being_y1 = current_map_cell_y0 + self.map_cell_size / 2
                # assume player color, change if needed
                map_being_color = self.map_player_color
                if isinstance(being, enemy.Enemy):
                    # enemy has x offset but no y offset
                    being_x0 += self.map_cell_size / 2
                    being_x1 += self.map_cell_size / 2
                    map_being_color = self.map_enemy_color
                being.graphical_id = self.map.create_rectangle(being_x0, being_y0, being_x1, being_y1, fill=map_being_color)

            # draw exits

            # draw items?

    # add back in later to make redrawing the map faster and less expensive?!
    # def remove_map_data_item(self, old_id):
    #     self.map.delete(old_id)
        
    def mainloop(self):
        self.root.mainloop()

class ModelNotInitiializedError(Exception):
    pass
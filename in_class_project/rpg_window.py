import tkinter as tk

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

    def set_underlying_model(self, proposed_model):
        self.model = proposed_model
        
    def mainloop(self):
        self.root.mainloop()

class ModelNotInitiializedError(Exception):
    pass
import tkinter as tk

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
        self.submit = tk.Button(self.root, text="submit", command=self.get_input)
        self.submit.grid(column=5, row=2, columnspan=1)

    def insert_into_character(self, character_string: str):
        self.character.insert(tk.INSERT, character_string)

    def get_input(self):
        '''Get input from input box and try to parse and execute that command.'''
        input_string = self.input.get().lower()

        if input_string == "stats":
            self.output.insert(tk.END, self.character.get('1.0', tk.END))
        else:
            self.output.insert(tk.END, f"unknown command: {input_string}\n")

        self.output.yview(tk.END)
        
    def mainloop(self):
        self.root.mainloop()
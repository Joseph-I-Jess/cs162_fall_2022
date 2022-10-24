'''Let's make a GUI that shows search.'''

import tkinter as tk

"""
    ToDo:
        have errors in label on GUI blink before disappearing?
        xhow do we want to handle the text box accepting the return key as a newline character in its input? Should we clear the newline...?
            fixed by swapping to entry widget :)
"""

class Gui_search:
    '''Show some GUI serach components and layout capabilities.'''
    def update_label_text(self, new_text):
        '''Update label text with new_text'''
        
        self.label_string_var.set(new_text)


    # setup GUI components
    # this is called the View of a program in the Model-View-Controller (MVC) architecture
    def __init__(self):
        '''Initialize this GUI.'''
        self.root = tk.Tk()
        #self.root.geometry("650x560")
        self.root.title("Computer GUI")

        self.label_string_var = tk.StringVar(self.root, "hello?")
        zero_img = tk.PhotoImage() # zero sized image to set scale of label to pixels instead of character width and height...
        self.computer_label = tk.Label(self.root, textvariable=self.label_string_var, image=zero_img, compound=tk.CENTER, width=100, height=20)
        self.computer_label.grid(column=0, row=0)

        self.input_text = tk.Entry(self.root, width=10)
        self.input_text.grid(column=2, row=0)
        self.input_text.focus_set()
        self.input_text.bind('<Return>', lambda event: self.update_label_text(self.input_text.get()))

        self.canvas_output = tk.Canvas(self.root, width=640, height=480, background="black")
        self.canvas_output.grid(column=0, row=3, columnspan=3)
        self.canvas_object_ids = []
        list_of_colors = ["red", "green", "blue"]
        for count in range(0,6):
            new_shape = self.canvas_output.create_rectangle(10 * count, 10, 10 * count + 10, 20, fill=list_of_colors[count % len(list_of_colors)])
            self.canvas_object_ids.append(new_shape)

        # setup data objects
        # this is called the Model of a program in the MVC architecture


        # connect data objects with GUI components
        # this is called the Controller of a program in the MVC architecture

    def mainloop(self):
        '''Start this GUI.'''
        self.root.mainloop()

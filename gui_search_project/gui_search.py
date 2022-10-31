'''Let's make a GUI that shows search.'''

import random
import time
import tkinter as tk

import rectangle.rectangle as rectangle

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

    
    def add_rectangle(self, x0, y0, x1, y1, fill_color):
        '''Create a rectangle, add it to canvas and rectangles list.'''
        new_rectangle = rectangle.Rectangle(0, x0, y0, x1, y1, fill_color)
        new_id = self.canvas_output.create_rectangle(new_rectangle.x0, new_rectangle.y0, new_rectangle.x1, new_rectangle.y1, fill=new_rectangle.fill_color)
        self.canvas_output.create_text(x0 + 10, y0 + 10, text=f"{y0 - y1}", fill="white")
        new_rectangle.id = new_id
        self.rectangles.append(new_rectangle)

    def search(self, proposed_number=None):
        # reset all rectangles to white
        for rectangle in self.rectangles:
            self.canvas_output.itemconfig(rectangle.id, fill="white")
        self.root.after(0, self.root.update())
        
        # fetch value from entry box
        if proposed_number is None:
            # should do input validation!
            proposed_number = int(self.input_text.get())

        # look through rectangles for that value
        for position, current_rectangle in enumerate(self.rectangles):
            # fetch delay from slider live as we run thr program...
            delay = self.slider.get()
            self.canvas_output.itemconfig(current_rectangle.id, fill="yellow")
            self.root.after(delay, self.root.update())
            if proposed_number == (current_rectangle.y0 - current_rectangle.y1):
                # change fill of current rectangle to yellow, pause, then change to white
                # We could use update and sleep... or we can cleverly plan ahead with the after method
                # self.root.update()
                # time.sleep(3)
                # change fill_color of any matching rectangles to white
                self.canvas_output.itemconfig(current_rectangle.id, fill="green")
                self.root.after(delay * 2, self.root.update())
            else:
                self.canvas_output.itemconfig(current_rectangle.id, fill="red")
                self.root.after(delay * 2, self.root.update())
                
        

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
        self.input_text.bind('<Return>', lambda event: self.search())

        self.canavs_output_height = 150
        self.canavs_output_width = 640
        self.canvas_output = tk.Canvas(self.root, width=self.canavs_output_width, height=self.canavs_output_height, background="black")
        self.canvas_output.grid(column=0, row=3, columnspan=3)

        self.slider = tk.Scale(self.root, from_=10, to=2000, orient="horizontal")
        self.slider.grid(column=1, row=0)

        # data objects
        self.rectangles = []
        width = 30
        # height will be random in the end
        x_offset = 20
        x_buffer = 10
        y_bottom_offset = 20
        for count in range(0,10):
            x0 = count * (width + x_buffer) + x_offset
            y0 = self.canavs_output_height - y_bottom_offset
            x1 = count * (width + x_buffer) + x_offset + width
            # should probably have min, max, and step be variables...
            y1 = self.canavs_output_height - y_bottom_offset - random.randrange(10, 110, 10)
            fill_color = "blue"
            self.add_rectangle(x0, y0, x1, y1, fill_color)
            

        # setup data objects
        # this is called the Model of a program in the MVC architecture


        # connect data objects with GUI components
        # this is called the Controller of a program in the MVC architecture

    def mainloop(self):
        '''Start this GUI.'''
        self.root.mainloop()

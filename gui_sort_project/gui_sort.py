'''Let's make a GUI that shows sorting.'''

import random
import time
import tkinter as tk

import rectangle.rectangle as rectangle

"""
    ToDo:
        !!!Change sort_step code to use rctangles list (model) for logic instead of canvas object ids (view)!!!
        have errors in label on GUI blink before disappearing?
        xhow do we want to handle the text box accepting the return key as a newline character in its input? Should we clear the newline...?
            fixed by swapping to entry widget :)
"""

class Gui_sort:
    '''Show some GUI sort components and layout capabilities.'''
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

    def highlight_rectangle_for_a_time(self, proposed_rectangle):
        '''Highlight a rectangle for an amount of time, then un-highlight that rectangle.'''
        print("highlight being called")
        # fetch delay from slider live as we run thr program...
        delay = self.slider.get()
        # fetch old oclor to change back later
        old_color = self.canvas_output.itemcget(proposed_rectangle.id, "fill")
        # update color of rectangle to "highlight" it
        self.canvas_output.itemconfig(proposed_rectangle.id, fill="yellow")
        # update color of data model rectangle being "highlighted"
        proposed_rectangle.fill_color = "yellow"
        # update the GUI to reflect change of data
        self.root.after(0, self.root.update())
        # change rectangle color back to original color
        self.root.after(delay, self.canvas_output.itemconfig(proposed_rectangle.id, fill=old_color))
        # should we package up the color changes...?
        proposed_rectangle.fill_color = old_color
        self.root.after(2 * delay, self.root.update())


    def sort_step(self):
        '''Perform one step of a sorting algorithm.'''
        # find next spot that needs sorted
        # let's just swap first two values if needed...
        # swap two values if needed
        rect0 = self.rectangles[0]
        rect1 = self.rectangles[1]
        rect0_height = rect0.y0 - rect0.y1
        rect1_height = rect1.y0 - rect1.y1
        if rect0_height > rect1_height:
            # swap them (ask canvas to swap x values of proposed rectangles)
            rect0_coords = self.canvas_output.coords(rect0.id)
            rect1_coords = self.canvas_output.coords(rect1.id)

            # swap x values of rect0_coords with rect1_coords
            #   similar to this tuple values swap
            #   x, y = y, x
            rect0_coords[0], rect0_coords[2], rect1_coords[0], rect1_coords[2] = \
                rect1_coords[0], rect1_coords[2], rect0_coords[0], rect0_coords[2]
            # remember to ask the cavas to reflect that!
            self.canvas_output.coords(rect0.id, rect0_coords)
            self.canvas_output.coords(rect1.id, rect1_coords)
            # we should also update our model rectangle objects x coords!!!

            # also swap x positions of the rectangle's associated label!
            """ Important note!!! +1 after rect0.id and rect1.id is because we know the order
                    that these objects were created in!!!
            """
            rect0_label_coords = self.canvas_output.coords(rect0.id + 1)
            rect1_label_coords = self.canvas_output.coords(rect1.id + 1)

            # swap x values of rect0_label_coords with rect1_label_coords
            rect0_label_coords[0], rect1_label_coords[0] = \
                rect1_label_coords[0], rect0_label_coords[0]
            # remember to ask the cavas to reflect that!
            self.canvas_output.coords(rect0.id + 1, rect0_label_coords)
            self.canvas_output.coords(rect1.id + 1, rect1_label_coords)
            
        

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
        self.input_text.bind('<Return>', lambda event: self.sort_step())

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

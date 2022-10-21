'''Let's make a basic GUI at least show up on the screen.'''

import tkinter as tk

from computer_project import computer

"""
    ToDo:
        have errors in label on GUI blink before disappearing
"""

class Gui_basics:
    '''Show some basic GUI components and layout capabilities.'''
    def update_label_text(self, new_text=None):
        '''Update label text with text from text box.'''
        # self.computer_label_string_var.set(f"{self.my_pc}")
        if new_text is None:
            new_text = self.input_text.get('1.0','end')
        
        self.computer_label_string_var.set(new_text)

    def move_canavs_object(self, move_x, move_y, proposed_index=None):
        if proposed_index is None:
            object_index = self.input_text.get('1.0', 'end').strip()
        else:
            object_index = proposed_index

        if object_index.isnumeric():
            object_index = int(object_index)
            if object_index > 0 and object_index <= len(self.canvas_object_ids):
                self.canvas_output.move(object_index, move_x, move_y)
            else:
                # should this show up on the GUI and blink a few times before disappearing?
                print(f"object index is out of range ({object_index})")
        elif object_index == "all":
            for index in self.canvas_object_ids:
                self.canvas_output.move(index, move_x, move_y)
        else:
            print(f"object index is invalid ({object_index})")

    def move_canavs_object_right_repeatedly(self, move_x, move_y, proposed_index=None):
        if proposed_index is None:
            object_index = self.input_text.get('1.0', 'end').strip()
        else:
            object_index = proposed_index
        
        self.move_canavs_object(move_x, move_y, object_index)

        # Note: if we click the button multiple times, then we have multiple "threads" running this code.
        self.root.after(1000, lambda: self.move_canavs_object_right_repeatedly(move_x, move_y, object_index))


    def create_new_window(self):
        """Create a new window with a label on it."""
        # should we create a list of windows for our program!?
        if self.new_window is None:
            print(f"Creating a new window!")
            self.new_window = tk.Toplevel(self.root)
            self.new_window.title("a new window")
            self.new_window.geometry("200x200")
            
            new_label = tk.Label(self.new_window, text="a new label on a new window!")
            new_label.pack()

            show_main_window_button = tk.Button(self.new_window, text="show main window", command=self.show_main_window)
            show_main_window_button.pack()

            self.new_window_text = tk.Text(self.new_window, width=10)
            self.new_window_text.pack()
        else:
            self.new_window.deiconify()

        self.root.withdraw()
        self.new_window_text.focus_force()

    def show_main_window(self):
        self.root.deiconify()
        self.new_window.withdraw()
        self.input_text.focus_force()

    def arrow_handler(self, event):
        # debug
        # print(f"event: {event}")
        if event.keysym == "Left":
            self.move_canavs_object(-10, 0)
        elif event.keysym == "Right":
            self.move_canavs_object(10, 0)
        elif event.keysym == "Up":
            self.move_canavs_object(0, -10)
        elif event.keysym == "Down":
            self.move_canavs_object(0, 10)

    def print_diagnostics(self):
        for key,value in self.__dict__.items():
            print(f"k: {key}, v: {value}")
            if hasattr(value, "__dict__"):
                for k,v in value.__dict__.items():
                    print(f"\tsk: {k}, sv: {v}")


    # setup GUI components
    # this is called the View of a program in the Model-View-Controller (MVC) architecture
    def __init__(self):
        '''Initialize this GUI.'''
        self.root = tk.Tk()
        #self.root.geometry("650x560")
        self.root.title("Computer GUI")

        self.computer_label_string_var = tk.StringVar(self.root, "hello?")
        zero_img = tk.PhotoImage() # zero sized image to set scale of label to pixels instead of character width and height...
        self.computer_label = tk.Label(self.root, textvariable=self.computer_label_string_var, image=zero_img, compound=tk.CENTER, width=100, height=20)
        self.computer_label.grid(column=0, row=0)

        self.label_a1 = tk.Label(self.root, text="A1")
        self.label_a1.grid(column=0, row=1)

        self.label_a2 = tk.Label(self.root, text="A2")
        self.label_a2.grid(column=0, row=2)

        self.label_b0 = tk.Label(self.root, text="B0")
        self.label_b0.grid(column=1, row=0)

        self.label_b1 = tk.Label(self.root, text="B1")
        self.label_b1.grid(column=1, row=1)

        self.update_label_button = tk.Button(self.root, text="update label", command=self.update_label_text)
        self.update_label_button.grid(column=1, row=2)

        self.move_canavs_object_right_button = tk.Button(
            self.root,
            text="Right",
            command=lambda: self.move_canavs_object(10, 0))
        self.move_canavs_object_right_button.grid(column=5, row=2)

        self.move_canavs_object_left_button = tk.Button(
            self.root,
            text="Left",
            command=lambda: self.move_canavs_object(-10, 0))
        self.move_canavs_object_left_button.grid(column=3, row=2)

        self.move_canavs_object_up_button = tk.Button(
            self.root,
            text="Up",
            command=lambda: self.move_canavs_object(0, -10))
        self.move_canavs_object_up_button.grid(column=4, row=1)

        self.move_canavs_object_down_button = tk.Button(
            self.root,
            text="Down",
            command=lambda: self.move_canavs_object(0, 10))
        self.move_canavs_object_down_button.grid(column=4, row=2)

        self.move_canavs_object_1_right_repeatedly_button = tk.Button(
            self.root,
            text="Move object 1 right repeatedly",
            command=lambda: self.move_canavs_object_right_repeatedly(10, 0, "1"))
        self.move_canavs_object_1_right_repeatedly_button.grid(column=4, row=3)

        self.move_canavs_object_right_repeatedly_button = tk.Button(
            self.root,
            text="Move object selected by text box right repeatedly",
            command=lambda: self.move_canavs_object_right_repeatedly(10, 0))
        self.move_canavs_object_right_repeatedly_button.grid(column=4, row=4)

        self.diagnostic_button = tk.Button(self.root, text="diagnotsics", command=self.print_diagnostics)
        self.diagnostic_button.grid(column=0, row=4)

        self.input_text = tk.Text(self.root, width=10, height=1)
        self.input_text.grid(column=2, row=0)
        self.input_text.focus_set()

        self.canvas_output = tk.Canvas(self.root, width=640, height=480, background="black")
        self.canvas_output.grid(column=0, row=3, columnspan=3)
        self.canvas_object_ids = []
        list_of_colors = ["red", "green", "blue"]
        for count in range(0,6):
            new_shape = self.canvas_output.create_rectangle(10 * count, 10, 10 * count + 10, 20, fill=list_of_colors[count % len(list_of_colors)])
            self.canvas_object_ids.append(new_shape)

        self.root.bind("<Key>", self.arrow_handler)



        # new window stuff
        self.new_window = None

        # Button for creating a new window.
        self.new_window_button = tk.Button(self.root, text="Show sub-window", command=self.create_new_window)
        self.new_window_button.grid(column=2, row=1)
        
        # debug
        # print(f"my_rectangle1_id: {my_rectangle1_id}")
        # print(f"my_rectangle2_id: {my_rectangle2_id}")
        # print(f"my_rectangle3_id: {my_rectangle3_id}")

        # setup data objects
        # this is called the Model of a program in the MVC architecture
        self.my_pc = computer.Computer()
        self.my_pc.toggle_power()
        
        # debug
        # print(f"self.my_pc: {self.my_pc}")


        # connect data objects with GUI components
        # this is called the Controller of a program in the MVC architecture

        # debug
        # self.root.update()
        # print(f"self.root.winfo_width: {self.root.winfo_width()}")
        # print(f"self.root.winfo_height: {self.root.winfo_height()}")

    def mainloop(self):
        '''Start this GUI.'''
        self.root.mainloop()

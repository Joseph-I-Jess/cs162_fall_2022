'''Let's make a basic GUI at least show up on the screen.'''

import tkinter as tk

from computer_project import computer


class Gui_basics:
    '''Show some basic GUI components and layout capabilities.'''
    def update_label_text(self, new_text=None):
        '''Update label text with text from text box.'''
        # self.computer_label_string_var.set(f"{self.my_pc}")
        if new_text is None:
            new_text = self.input_text.get('1.0','end')
        
        self.computer_label_string_var.set(new_text)

    def move_canavs_object(self, object_index, move_x, move_y):
        self.canvas_output.move(object_index, move_x, move_y)

    # setup GUI components
    # this is called the View of a program in the Model-View-Controller (MVC) architecture
    def __init__(self):
        '''Initialize this GUI.'''
        self.root = tk.Tk()
        #self.root.geometry("650x560")
        self.root.title("Computer GUI")

        self.computer_label_string_var = tk.StringVar(self.root, "hello?")
        self.computer_label = tk.Label(self.root, textvariable=self.computer_label_string_var, width=20)
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

        # this code is easy to break, because we are not validating input yet...!
        self.move_canavs_object_right_button = tk.Button(self.root, text="Right", command=lambda: self.move_canavs_object(int(self.input_text.get('1.0', 'end')), 10, 0))
        self.move_canavs_object_right_button.grid(column=5, row=2)

        # this code is easy to break, because we are not validating input yet...!
        self.move_canavs_object_left_button = tk.Button(self.root, text="Left", command=lambda: self.move_canavs_object(int(self.input_text.get('1.0', 'end')), -10, 0))
        self.move_canavs_object_left_button.grid(column=3, row=2)

        # this code is easy to break, because we are not validating input yet...!
        self.move_canavs_object_up_button = tk.Button(self.root, text="Up", command=lambda: self.move_canavs_object(int(self.input_text.get('1.0', 'end')), 0, -10))
        self.move_canavs_object_up_button.grid(column=4, row=1)

        # this code is easy to break, because we are not validating input yet...!
        self.move_canavs_object_down_button = tk.Button(self.root, text="Down", command=lambda: self.move_canavs_object(int(self.input_text.get('1.0', 'end')), 0, 10))
        self.move_canavs_object_down_button.grid(column=4, row=2)

        self.input_text = tk.Text(self.root, width=10, height=1)
        self.input_text.grid(column=2, row=0)

        self.canvas_output = tk.Canvas(self.root, width=640, height=480, background="black")
        self.canvas_output.grid(column=0, row=3, columnspan=3)
        my_rectangle1_id = self.canvas_output.create_rectangle(10, 10, 20, 20, fill="red")
        my_rectangle2_id = self.canvas_output.create_rectangle(30, 10, 40, 20, fill="green")
        my_rectangle3_id = self.canvas_output.create_rectangle(10, 30, 20, 40, fill="blue")
        
        # debug
        # print(f"my_rectangle1_id: {my_rectangle1_id}")
        # print(f"my_rectangle2_id: {my_rectangle2_id}")
        # print(f"my_rectangle3_id: {my_rectangle3_id}")

        # setup data objects
        # this is called the Model of a program in the MVC architecture
        self.my_pc = computer.Computer()
        print(f"self.my_pc: {self.my_pc}")


        # connect data objects with GUI components
        # this is called the Controller of a program in the MVC architecture

        # debug
        # self.root.update()
        # print(f"self.root.winfo_width: {self.root.winfo_width()}")
        # print(f"self.root.winfo_height: {self.root.winfo_height()}")

    def mainloop(self):
        '''Start this GUI.'''
        self.root.mainloop()

'''Let's make a basic GUI at least show up on the screen.'''

import sys
import tkinter as tk

from computer_project import computer

def update_label_text():
    # computer_label_string_var.set(f"{my_pc}")
    computer_label_string_var.set(input_text.get('1.0','end'))

# setup GUI components
# this is called the View of a program in the Model-View-Controller (MVC) architecture
root = tk.Tk()
root.geometry("300x200")
root.title("Computer GUI")

computer_label_string_var = tk.StringVar(root, "hello?")
computer_label = tk.Label(root, textvariable=computer_label_string_var, width=20)
computer_label.grid(column=0, row=0)

label_a1 = tk.Label(root, text="A1")
label_a1.grid(column=0, row=1)

label_a2 = tk.Label(root, text="A2")
label_a2.grid(column=0, row=2)

label_b0 = tk.Label(root, text="B0")
label_b0.grid(column=1, row=0)

label_b1 = tk.Label(root, text="B1")
label_b1.grid(column=1, row=1)



update_label_button = tk.Button(root, text="update label", command=update_label_text)
update_label_button.grid(column=1, row=2)

input_text = tk.Text(root, width=10, height=1)
input_text.grid(column=2, row=0)


# setup data objects
# this is called the Model of a program in the MVC architecture
my_pc = computer.Computer()
print(f"my_pc: {my_pc}")


# connect data objects with GUI components
# this is called the Controller of a program in the MVC architecture


root.mainloop()

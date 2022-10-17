import gui_basics_project.gui_basics

def test_root_not_none():
    test_gui = gui_basics_project.gui_basics.Gui_basics()
    print(f"type(test_gui.root): {type(test_gui.root)}")

test_root_not_none()

# my_gui = gui_basics_project.gui_basics.Gui_basics()
# my_gui.update_label_text("This is some new text!")

# my_gui.mainloop()

print("Got to the end of main!")

'''
ToDo:
    Make class out of gui_basics.py and create a main method and main guard in this file?
'''
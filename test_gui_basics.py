import tkinter as tk

import gui_basics_project.gui_basics

def test_root_not_none():
    test_gui = gui_basics_project.gui_basics.Gui_basics()
    
    expected_result = True
    actual_result = type(test_gui.root) is not None

    print(f"type(test_gui.root) is not None: {actual_result}")

    assert actual_result

def test_root_is_tk():
    test_gui = gui_basics_project.gui_basics.Gui_basics()
    
    expected_result = tk.Tk
    actual_result = type(test_gui.root)  == expected_result

    print(f"type(test_gui.root) == expected_result: {actual_result}")

def test_gui_width_less_than_2560():

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # important note for us in the future: we need the GUI to show to have a size to actually compare against!
    test_gui = gui_basics_project.gui_basics.Gui_basics()
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # come back and work with monkey patch and such...
    # test_gui.mainloop()

    gui_geometry_width = int(test_gui.root.geometry().split('x')[0])
    print(f"gui_geometry_width: {gui_geometry_width}")
    # int(test_gui.root.geometry.split('x')[0])

    comparison_value = 2560
    actual_result = gui_geometry_width < comparison_value

    assert actual_result

# demo final project

import in_class_project.rpg as rpg
import in_class_project.rpg_window as rpg_window

main_window = rpg_window.Rpg_window()
model = rpg.Rpg()

main_window.insert_into_character(model.get_player_string())

main_window.mainloop()

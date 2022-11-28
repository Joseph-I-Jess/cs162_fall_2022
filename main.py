# demo final project

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Note to Joseph for week 10 of CS162 fall 2022!
#
# Remember to mention that the basics of each
#   of these parts is totally fine!
#
# And that you have built roughly this game
#   something like 9 times before
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import in_class_project.rpg as rpg
import in_class_project.rpg_window as rpg_window

main_window = rpg_window.Rpg_window()
model = rpg.Rpg()

main_window.set_underlying_model(model)

main_window.insert_into_character(model.get_player_string())

main_window.mainloop()

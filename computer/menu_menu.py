'''Test whether import in multiple files imports multiple times.

In the end, no it does not, only one import runs.'''

import computer
import computer_menu

print(f"__name__ in my menu_menu file: {__name__}")

print(f"computer.PI: {computer.PI}")

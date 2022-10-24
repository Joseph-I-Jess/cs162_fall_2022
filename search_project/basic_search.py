# Demonstrate basic search techniques in Python.

my_numbers = [5, 2, 7, 8, 7, 2, 3, 9, 4, 3, 6, 8, 12, 4, 7, 9]

print(f"my_numbers(n = {len(my_numbers)}): {my_numbers}")

# find a number in the list?
# we should be validating this!
proposed_number = int(input("Please enter a number to search forin our list: "))
is_proposed_number_in_list = False
index_of_proposed_number_in_list = -1
indices_of_proposed_number_in_list = []

# I normally want you to use these kinds of shortcuts...
# If the assignment is about this kind of shortcut, do not use those shortcuts.
# is_proposed_number_in_list = proposed_number in my_numbers


# If all I care about is finding if the value is in the list, then this works fine:
# But what if I want or need the index of the matched value?
# for element in my_numbers:
#     if element == proposed_number:
#         is_proposed_number_in_list = True
#         break

# find whether the proposed number is in the list and its index or -1 index if not found
# for index,element in enumerate(my_numbers):
#     if element == proposed_number:
#         is_proposed_number_in_list = True
#         index_of_proposed_number_in_list = index
#         break

# print(f"is_proposed_number_in_list: {is_proposed_number_in_list}, found at index: {index_of_proposed_number_in_list}")

# find all indices that match the proposed number :)!
for index,element in enumerate(my_numbers):
    if element == proposed_number:
        is_proposed_number_in_list = True
        indices_of_proposed_number_in_list.append(index)

print(f"is_proposed_number_in_list: {is_proposed_number_in_list}, found at indices: {indices_of_proposed_number_in_list}")

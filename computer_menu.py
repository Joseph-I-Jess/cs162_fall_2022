'''Program to interact with Computer objects.'''

import computer

debug_level = 0

def main():
    #menu program
    user_input = "-1"
    first_run = True
    while user_input != "0":
        #Display a menu, ask user for input, and vlidate the input.
        bad_input = True
        while bad_input == True:
            user_input = input(
                f"0: quit\n" \
                "1: input computer computer specifications\n" \
                "2: display current computer specifications\n" \
                "3: toggle power on current computer\n" \
                "What would you like to do?\n"
                )

            if user_input not in ["0", "1", "2", "3"]:
                print(f"That is not a valid input")
            else:
                bad_input = False

        #run user's requested input
        if first_run:
            my_computer = None

        if user_input == "1":
            #if 1 request inputs from user for Computer object
            new_computer_name = input(f"What is your computer's name?\n")
            new_cpu_model = input(f"\nWhat is your CPU model?\n")
            my_computer = computer.Computer(new_computer_name, new_cpu_model)
        elif user_input == "2":
            #if 2 display current Computer object if it exists
            if my_computer == None:
                print("You have not created a computer yet.")
            else:
                print(my_computer)
        elif user_input == "3":
            #toggle power on current computer
            if my_computer != None:
                my_computer.toggle_power()
                if my_computer.powered_on:
                    print("Your computer is now on!")
                else:
                    print("Your computer is now off.")
            else:
                print("You have not created a computer yet.")
        elif user_input == "0":
            #if 0 quit
            pass

        first_run = False

    print("Thank you for playing!")

print(f"__name__ in my computer_menu file: {__name__}")
if __name__ == "__main__":
    main()

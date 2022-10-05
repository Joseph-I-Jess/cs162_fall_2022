#Demonstrate some basic Python code for CS162.

debug_level = 0

# value = 25

# def dublin(value: int):
#     '''Dublin takes a value and returns double that value.
    
#     This is not a complicated function, expecting an int as input and
#     returning an int.
#     '''
#     return value * 2

# dublin_return = dublin(5)

# if debug_level > 0:
#     print(f"dublin_return: {dublin_return}")

# x = 2

# x = int(input("Input what x is: "))

# if x == 42:
#     print(f"x*2: {x*2}")
# else:
#     print(f"x: {x}")

# while x >= 0:
#     print(f"hello! (x: {x})")
#     x -= 1

class Computer:

    def __init__(
        self,
        new_name = "no name given",
        new_cpu_name = "i7",
        new_cpu_freq_value = 3.9,
        new_cpu_freq_unit = "GHz",
        new_motherboard = "Gigabyte G276",
        new_motherboard_ram_slots = 4,
        new_motherboard_ram_max_size = 2**30 * 16,
        new_powered_on = False
        ):
        self.name = new_name

        self.cpu_name = new_cpu_name
        self.cpu_freq_value = new_cpu_freq_value
        self.cpu_freq_unit = new_cpu_freq_unit

        self.motherboard = new_motherboard
        self.motherboard_ram_slots = new_motherboard_ram_slots
        #2**30 is a gibibyte and * 16 because this board only supports up to 16GB
        self.motherboard_ram_max_size = new_motherboard_ram_max_size

        self.powered_on = new_powered_on

    def toggle_power(self):
        '''Toggle the powered_on attribute of this computer.'''
        self.powered_on = not self.powered_on

    def __str__(self):
        '''Represent this computer as a string or return that the computer is off.'''
        if self.powered_on == False:
            result = "System is powered off!"
        else:
            result = f"self.name: {self.name}:\n" \
            f"\tself.cpu_name: {self.cpu_name}\n" \
            f"\tself.cpu_freq_value: {self.cpu_freq_value}\n" \
            f"\tself.cpu_freq_unit: {self.cpu_freq_unit}\n" \
            f"\tself.motherboard: {self.motherboard}\n" \
            f"\tself.motherboard_ram_slots: {self.motherboard_ram_slots}\n" \
            f"\tself.motherboard_ram_max_size: {self.motherboard_ram_max_size}\n" \
            f"\tself.powered_on: {self.powered_on}"

        return result
        


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
        my_computer = Computer(new_computer_name, new_cpu_model)
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

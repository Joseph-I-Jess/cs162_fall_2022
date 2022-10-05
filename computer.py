'''Class to describe a computer object.'''

print(f"__name__ in my computer file: {__name__}")

PI = 3.14159265358979323

class Cpu:
    pass

class Ram:
    pass

class Psu:
    pass

class Computer:

    def __init__(
        self,
        new_name : str = "no name given",
        new_cpu_name : str = "i7",
        new_cpu_freq_value : float = 3.9,
        new_cpu_freq_unit : str = "GHz",
        new_motherboard : str = "Gigabyte G276",
        new_motherboard_ram_slots : int = 4,
        new_motherboard_ram_max_size : int = 2**30 * 16,
        new_powered_on : bool = False
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
        
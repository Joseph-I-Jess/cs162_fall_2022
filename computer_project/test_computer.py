import computer_project.computer

"""ToDo:
        show smarter way to test multiple internal variables (try my_pc's dictionary of internal objects)
        show smarter way to test long formatted string from file (try my_pc's __str__ output in a file).
"""

def test_default_computer():
    my_pc = computer_project.computer.Computer()

    expected_name: str = "no name given"
    expected_cpu_name: str = "i7"
    expected_cpu_freq_value: float = 3.9
    expected_cpu_freq_unit: str = "GHz"
    expected_motherboard: str = "Gigabyte G276"
    expected_motherboard_ram_slots: int = 4
    expected_motherboard_ram_max_size: int = 2**30 * 16
    expected_powered_on: bool = False

    actual_name = my_pc.name
    actual_cpu_name = my_pc.cpu_name
    actual_cpu_freq_value = my_pc.cpu_freq_value
    actual_cpu_freq_unit = my_pc.cpu_freq_unit
    actual_motherboard = my_pc.motherboard
    actual_motherboard_ram_slots = my_pc.motherboard_ram_slots
    actual_motherboard_ram_max_size = my_pc.motherboard_ram_max_size
    actual_powered_on = my_pc.powered_on

    assert expected_name == actual_name
    assert expected_cpu_name == actual_cpu_name
    assert expected_cpu_freq_value == actual_cpu_freq_value
    assert expected_cpu_freq_unit == actual_cpu_freq_unit
    assert expected_motherboard == actual_motherboard
    assert expected_motherboard_ram_slots == actual_motherboard_ram_slots
    assert expected_motherboard_ram_max_size == actual_motherboard_ram_max_size
    assert expected_powered_on == actual_powered_on

def test_default_computer_str():
    my_pc = computer_project.computer.Computer()

    expected_result = "System is powered off!"
    actual_result = my_pc.__str__()
    # similar to
    # actual_result = f"{my_pc}"

    assert actual_result == expected_result

def test_powered_on_computer_str():
    my_pc = computer_project.computer.Computer()
    my_pc.toggle_power()

    # messy!  Maybe use a file with these contents or manually format this to look better in code...
    expected_result = \
"""self.name: no name given:
\tself.cpu_name: i7
\tself.cpu_freq_value: 3.9
\tself.cpu_freq_unit: GHz
\tself.motherboard: Gigabyte G276
\tself.motherboard_ram_slots: 4
\tself.motherboard_ram_max_size: 17179869184
\tself.powered_on: True"""
    actual_result = my_pc.__str__()
    # similar to
    # actual_result = f"{my_pc}"

    assert actual_result == expected_result

def test_pi():
    expected_result = 3.14159265358979323
    actual_result = computer_project.computer.PI

    assert actual_result == expected_result

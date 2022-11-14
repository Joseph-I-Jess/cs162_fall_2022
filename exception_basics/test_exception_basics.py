'''Simple tests to get testing and coverage data working.'''

import pytest

import exception_basics.exceptions_basics as eb

def test_exceptions_basics_default_values():
    my_exceptions = eb.exception_basics()

    assert my_exceptions.name == "no name given"
    assert my_exceptions.age == 0
    assert my_exceptions.gender_identity == "no gender identity given"

def test_str_with_default_values():
    my_exceptions = eb.exception_basics()

    name = "no name given"
    age = 0
    gender_identity = "no gender identity given"

    actual_result = my_exceptions.__str__()
    expected_result = f"name: {name}, age: {age}, gender identity: {gender_identity}"

    assert expected_result == actual_result

def test_str_with_custom_values():
    name = "Joseph"
    age = 36
    gender_identity = "male"

    my_exceptions = eb.exception_basics(name, age, gender_identity)

    actual_result = my_exceptions.__str__()
    expected_result = f"name: {name}, age: {age}, gender identity: {gender_identity}"

    assert expected_result == actual_result

def test_driving_age_ratio_with_default_values():
    my_exceptions = eb.exception_basics()

    actual_result = my_exceptions.driving_age_ratio()
    expected_result = -1

    assert expected_result == actual_result

def test_driving_age_ratio_with_good_custom_values():
    age = 8
    
    my_exceptions = eb.exception_basics(new_age=age)

    actual_result = my_exceptions.driving_age_ratio()
    expected_result = 0.5

    assert expected_result == actual_result

def test_driving_age_ratio_with_bad_custom_values():
    age = -48 # we do not expect a negative age, but the program is fine with it
    
    my_exceptions = eb.exception_basics(new_age=age)

    actual_result = my_exceptions.driving_age_ratio()
    expected_result = -3

    assert expected_result == actual_result

def test_lifespan_age_ratio_with_good_custom_values():
    age = 36
    
    my_exceptions = eb.exception_basics(new_age=age)

    actual_result = my_exceptions.lifespan_age_ratio()
    expected_result = 0.5

    assert expected_result == actual_result

def test_lifespan_age_ratio_with_age_negative_1():
    age = -1
    
    my_exceptions = eb.exception_basics(new_age=age)

    actual_result = my_exceptions.lifespan_age_ratio()
    expected_result = -42

    assert expected_result == actual_result

def test_lifespan_age_ratio_with_age_0_exception():
    age = 0
    
    my_exceptions = eb.exception_basics(new_age=age)

    with pytest.raises(eb.Some_exception) as e_info:
        actual_result = my_exceptions.lifespan_age_ratio()

    # expecting some exception so no explicit assert is required

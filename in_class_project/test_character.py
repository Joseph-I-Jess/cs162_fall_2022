'''Test the character class.'''

import character
import item

def test_default_character_stats():
    #block of expected values
    expected_character_name = "test_default_character_stats"
    expected_character_default_attack = character.Character.DEFAULT_ATTACK
    expected_character_default_defense = character.Character.DEFAULT_DEFENSE
    expected_character_default_health = character.Character.DEFAULT_HEALTH
    # do the same for other default values in the character object or class!

    # create the thing to be tested based on inputs from expceted values (might be inputs that create those expected values)
    test_character = character.Character(name=expected_character_name)

    # fetch actual values of test object
    actual_character_name = test_character.name
    actual_character_attack = test_character.attack
    actual_character_defense = test_character.defense
    actual_character_health = test_character.health

    #compare expected values to the actual values of the test object
    assert actual_character_name == expected_character_name
    assert actual_character_attack == expected_character_default_attack
    assert actual_character_defense == expected_character_default_defense
    assert actual_character_health == expected_character_default_health

def test_custom_character_stats():
    expected_character_name = "custom character"
    expected_character_attack = 12
    expected_character_defense = 2
    expected_character_health = 99

    test_character = character.Character(name=expected_character_name, attack=expected_character_attack, defense=expected_character_defense, health=expected_character_health)

    actual_character_name = test_character.name
    actual_character_attack = test_character.attack
    actual_character_defense = test_character.defense
    actual_character_health = test_character.health

    assert actual_character_name == expected_character_name
    assert actual_character_attack == expected_character_attack
    assert actual_character_defense == expected_character_defense
    assert actual_character_health == expected_character_health


# should this be in a separate integration test file?
def test_character_equip():

    item_attack = 5
    item_defense = 1
    item_health = -1

    expected_character_name = "custom character equipment"
    expected_character_attack_with_equipment = character.Character.DEFAULT_ATTACK + item_attack
    expected_character_defense_with_equipment = character.Character.DEFAULT_DEFENSE + item_defense
    expected_character_health_with_equipment = character.Character.DEFAULT_HEALTH + item_health

    # create objects
    test_character = character.Character(name=expected_character_name)
    test_item = item.Item(attack=item_attack, defense=item_defense, health=item_health)

    # have objects interact... equipping the item in the character in this case!
    test_character.inventory[test_item.name] = test_item
    test_character.equip(["equip", test_item.name])

    actual_character_name = test_character.name
    actual_character_attack = test_character.attack
    actual_character_defense = test_character.defense
    actual_character_health = test_character.health

    assert actual_character_name == expected_character_name
    assert actual_character_attack == expected_character_attack_with_equipment
    assert actual_character_defense == expected_character_defense_with_equipment
    assert actual_character_health == expected_character_health_with_equipment

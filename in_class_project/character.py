'''Create and manage a character'''

import in_class_project.being as being

"""
    ToDo:
        should stats be a dictionary of stats for easier modification by items, powers, etc. later?
        Should some stats (or all stats) have a current stat and a maximum stat?
"""

class Character(being.Being):
    '''Player character class.'''

    # add type hints!?
    def __init__(self, graphical_id=None, location=None, name="hero", level=1, attack=being.Being.DEFAULT_ATTACK, defense=being.Being.DEFAULT_DEFENSE, health=being.Being.DEFAULT_HEALTH, inventory={}, equipment={}):
        super().__init__(graphical_id, location, name, level, attack, defense, health, inventory, equipment)

    def set_location(self, new_location=None):
        self.location = new_location

    def equip(self, proposed_equipment_names: list[str]) -> str:
        result = ""
        
        # in inventory but not yet equipped
        if len(proposed_equipment_names) >= 2 and proposed_equipment_names[1] in self.inventory and proposed_equipment_names[1] not in self.equipment:
            proposed_equipment_name = proposed_equipment_names[1]
            proposed_equipment = self.inventory[proposed_equipment_name]

            self.equipment[proposed_equipment_name] = proposed_equipment
            self.attack += proposed_equipment.attack
            self.defense += proposed_equipment.defense
            self.health += proposed_equipment.health

            result = f"equipped {proposed_equipment_name}"
        else:
            result = f"You do not have an item named {proposed_equipment_name}"

        return result

    def unequip(self, proposed_equipment_names: list[str]) -> str:
        result = ""
        
        # equipped
        if len(proposed_equipment_names) >= 2 and proposed_equipment_names[1] in self.equipment:
            proposed_equipment_name = proposed_equipment_names[1]
            proposed_equipment = self.equipment[proposed_equipment_name]

            self.equipment.pop(proposed_equipment_name, None)
            self.attack -= proposed_equipment.attack
            self.defense -= proposed_equipment.defense
            self.health -= proposed_equipment.health
            
            result = f"unequipped {proposed_equipment_name}"
        else:
            result = f"You do not have an item named {proposed_equipment_name} equipped"

        return result

'''Create and manage a character'''

"""
    ToDo:
        should stats be a dictionary of stats for easier modification by items, powers, etc. later?
"""

class Character:
    '''Player character class.'''
    
    DEFAULT_ATTACK = 10
    DEFAULT_DEFENSE = 10
    DEFAULT_HEALTH = 10

    # add type hints!?
    def __init__(self, graphical_id=None, location=None, name="hero", level=1, attack=DEFAULT_ATTACK, defense=DEFAULT_DEFENSE, health=DEFAULT_HEALTH, inventory={}, equipment={}):
        self.graphical_id = graphical_id # to be used if this object is drawn on a graphical space
        self.location = location
        self.name = name
        self.level = level
        
        self.attack = attack # damage on hit
        self.defense = defense # damage reduction when hit
        self.health = health
        
        self.inventory = inventory # all items the character carries
        self.equipment = equipment # items that are equipped on the character

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

    def __str__(self):
        result = f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"
        result += f"\nitems:"
        for item in self.inventory:
            result += "\n\t"
            if item in self.equipment:
                result += "(equipped) "
            result += f"{self.inventory[item].name}"

        return result
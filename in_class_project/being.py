'''Abstract class to represent characters and enemies in this game.'''

import in_class_project.game_object as game_object

class Being(game_object.Game_object):
    '''A being, which is either a character or an enemy.'''

    DEFAULT_ATTACK = 10
    DEFAULT_DEFENSE = 10
    DEFAULT_HEALTH = 10

    def __init__(self, graphical_id=None, graphics_file=None, location=None, name="being", level=1, attack=DEFAULT_ATTACK, defense=DEFAULT_DEFENSE, health=DEFAULT_HEALTH, inventory=None, equipment=None):
        super().__init__(graphical_id, graphics_file, location, name, attack, defense, health)
        self.level = level
        
        self.inventory = inventory if inventory is not None else list() # all items the character carries
        # input validation check on equipped items in equipment dictionary
        self.equipment = equipment if equipment is not None else dict() # items that are equipped on the character by the item equipment slot as the key and the item as the value
        self.equipment_slots = {}# equipment_slot to item equipped
        # initialize equipment slots with one per slot type
        for slot_name in game_object.Game_object.EQUIPMENT_SLOTS:
            self.equipment_slots[slot_name] = None

    def __str__(self):
        result = f"name: {self.name}\nlevel: {self.level}\nattack: {self.attack}\ndefense: {self.defense}\nhealth: {self.health}"
        result += f"\nitems:"
        for item in self.inventory:
            result += "\n\t"
            if item.name in self.equipment:
                result += "(equipped) "
            result += f"{item.name}"

        return result

    def equip(self, proposed_equipment_names: list[str]) -> str:
        result = ""
        
        # in inventory but not yet equipped
        if len(proposed_equipment_names) >= 2:
            # did we give enough arguments to the command?
            proposed_equipment_name = proposed_equipment_names[1]

            if any(proposed_equipment_name == item.name for item in self.inventory):
                #if any item has that name in inventory
                proposed_equipment = None
                for item in self.inventory:
                    if proposed_equipment_name == item.name:
                        proposed_equipment = item

                if proposed_equipment_name not in self.equipment:
                    # if that equipment is not already equipped
                    if self.equipment_slots[proposed_equipment.slot] is not None:
                        # if slot is in use already, then unequip old item
                        result += self.unequip(["unequip", self.equipment_slots[proposed_equipment.slot].name]) + "\n"

                    self.equipment[proposed_equipment_name] = proposed_equipment
                    self.equipment_slots[proposed_equipment.slot] = proposed_equipment
                    self.attack += proposed_equipment.attack
                    self.defense += proposed_equipment.defense
                    self.health += proposed_equipment.health

                    result += f"equipped {proposed_equipment_name}"
                else:
                    result += f"{proposed_equipment_name} is already equipped!"
            else:
                result += f"You do not have equipment named {proposed_equipment_name} in your inventory!"
        else:
            result = "What is it that you wanted to equip?"

        return result

    def unequip(self, proposed_equipment_names: list[str]) -> str:
        result = ""
        if len(proposed_equipment_names) >= 2:
            proposed_equipment_name = proposed_equipment_names[1]
        # equipped
        if proposed_equipment_name in self.equipment:
            proposed_equipment = self.equipment[proposed_equipment_name]

            self.equipment.pop(proposed_equipment_name, None)
            self.equipment_slots[proposed_equipment.slot] = None
            self.attack -= proposed_equipment.attack
            self.defense -= proposed_equipment.defense
            self.health -= proposed_equipment.health
            
            result = f"unequipped {proposed_equipment_name}"
        else:
            result = f"You do not have an item named {proposed_equipment_name} equipped"

        return result

'''Demonstrate basic inheritance.'''

class Mammal:
    def __init__(self, fur_color="brown"):
        self.fur_color = fur_color

class Cat(Mammal):
    def __init__(self, whiskers="straight", tail="long", fur_color="brown"):
        super().__init__(fur_color)
        self.type = "Cat" # this animals "type" of animal
        self.whiskers = whiskers
        self.tail = tail

    def vocalize(self):
        '''Return a string with the vocalization of this animal.'''
        return "meow"

    def __str__(self):
        '''Return a string representing this animal.'''
        return f"Type: {self.type}, whiskers: {self.whiskers}, tail: {self.tail}, fur color: {self.fur_color}"
    
class Tiger(Cat):
    def __init__(self, whiskers="straight", tail="long"):
        super().__init__(whiskers, tail, "orange")
        self.type = "Tiger" #override default value
        self.fur_pattern = "stripes"

    def vocalize(self):
        return "chuff"

    def __str__(self):
        return super().__str__() + f", fur pattern: {self.fur_pattern}"
        

class House_cat(Cat):
    def __init__(self, whiskers="straight", tail="short"):
        super().__init__(whiskers, tail)
        self.type = "House Cat"

''' Represent a rectangle's data ready for use in a GUI. '''

class Rectangle:
    '''A rectangle class.'''
    def __init__(self, new_id=0, new_x0=0, new_y0=0, new_x1=0, new_y1=0, new_fill_color="red"):
        self.id = new_id # set an id on this rectangle... perhaps this is the id of an associated Canvas object id
        self.x0 = new_x0
        self.y0 = new_y0
        self.x1 = new_x1
        self.y1 = new_y1
        self.fill_color = new_fill_color